if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {
    'openssh-server': {
        'installed': True,
    },
}

ssh_service_name = 'sshd'
permitrootlogin = 'prohibit-password'
if node.os == 'debian':
    ssh_service_name = 'ssh'
    permitrootlogin = 'without-password'

svc_systemd = {
    ssh_service_name: {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:openssh-server'],
    },
}

actions = {
    'ssh_generate_missing_host_keys': {
        'command': 'ssh-keygen -A',
        'triggered': True,
        'needs': ['pkg_apt:openssh-server'],
        'triggers': ['svc_systemd:{}:restart'.format(ssh_service_name)],
    },
}

files = {
    '/etc/ssh/sshd_config': {
        'source': 'sshd_config',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'password': node.metadata.get('ssh', {}).get('password', False),
            'permitrootlogin': permitrootlogin,
        },
        'needs': ['pkg_apt:openssh-server'],
        'triggers': [
            'action:ssh_generate_missing_host_keys',
            'svc_systemd:{}:restart'.format(ssh_service_name),
        ],
    },
}
