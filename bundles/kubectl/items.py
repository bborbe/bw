if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}
actions = {}
files = {}
directories = {}

if node.metadata.get('kubectl', {}).get('enabled', False):
    # Ensure keyrings directory exists
    directories['/etc/apt/keyrings'] = {
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
    }

    # Download and install Kubernetes GPG key
    version = node.metadata.get('kubectl', {}).get('version', 'v1.35')
    actions['install_kubernetes_gpg_key'] = {
        'command': 'curl -fsSL https://pkgs.k8s.io/core:/stable:/{version}/deb/Release.key | gpg --batch --yes --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg && chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg'.format(version=version),
        'unless': 'test -f /etc/apt/keyrings/kubernetes-apt-keyring.gpg',
        'needs': [
            'directory:/etc/apt/keyrings',
        ],
        'interactive': False,
    }

    # Add Kubernetes apt repository
    files['/etc/apt/sources.list.d/kubernetes.list'] = {
        'content': 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/{version}/deb/ /\n'.format(version=version),
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'needs': ['action:install_kubernetes_gpg_key'],
        'triggers': ['action:apt_update'],
    }

    # Install kubectl package
    pkg_apt['kubectl'] = {
        'installed': True,
        'needs': ['file:/etc/apt/sources.list.d/kubernetes.list'],
    }
else:
    # Clean up if disabled
    files['/etc/apt/sources.list.d/kubernetes.list'] = {
        'delete': True,
        'triggers': ['action:apt_update'],
    }
    files['/etc/apt/keyrings/kubernetes-apt-keyring.gpg'] = {
        'delete': True,
    }
    pkg_apt['kubectl'] = {
        'installed': False,
    }
