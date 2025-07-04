if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {
    'openssh-server': {
        'installed': True,
    },
}

ssh_service_name = 'ssh'
permitrootlogin = 'prohibit-password'
if node.os == 'raspbian' or node.os == 'debian':
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
            'password_authentication': node.metadata.get('ssh', {}).get('password_authentication', False),
            'x11_forwarding': node.metadata.get('ssh', {}).get('x11_forwarding', False),
            'allow_agent_forwarding': node.metadata.get('ssh', {}).get('allow_agent_forwarding', False),
            'permitrootlogin': permitrootlogin,
        },
        'needs': ['pkg_apt:openssh-server'],
        'triggers': [
            'action:ssh_generate_missing_host_keys',
            'svc_systemd:{}:restart'.format(ssh_service_name),
        ],
    },
}
