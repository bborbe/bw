os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'openssh-server': {
        'installed': True,
    },
}

svc_systemd = {
    'sshd': {
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
        'triggers': ['svc_systemd:sshd:restart'],
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
        },
        'needs': ['pkg_apt:openssh-server'],
        'triggers': [
            'action:ssh_generate_missing_host_keys',
            'svc_systemd:sshd:restart',
        ],
    },
}
