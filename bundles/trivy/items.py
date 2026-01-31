if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}
actions = {}
files = {}
directories = {}

if node.metadata.get('trivy', {}).get('enabled', False):
    # Download and install Trivy GPG key
    actions['install_trivy_gpg_key'] = {
        'command': 'mkdir -p /etc/apt/keyrings && curl -fsSL https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor -o /etc/apt/keyrings/trivy.gpg && chmod 644 /etc/apt/keyrings/trivy.gpg',
        'unless': 'test -f /etc/apt/keyrings/trivy.gpg',
    }

    # Add Trivy apt repository
    files['/etc/apt/sources.list.d/trivy.list'] = {
        'content': 'deb [signed-by=/etc/apt/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main\n',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'needs': ['action:install_trivy_gpg_key'],
        'triggers': ['action:apt_update'],
    }

    # Install trivy package
    pkg_apt['trivy'] = {
        'installed': True,
        'needs': ['file:/etc/apt/sources.list.d/trivy.list'],
    }
else:
    # Clean up if disabled
    files['/etc/apt/sources.list.d/trivy.list'] = {
        'delete': True,
        'triggers': ['action:apt_update'],
    }
    files['/etc/apt/keyrings/trivy.gpg'] = {
        'delete': True,
    }
    pkg_apt['trivy'] = {
        'installed': False,
    }
