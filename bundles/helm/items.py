actions = {}
files = {}
pkg_apt = {}

if node.metadata.get('helm', {}).get('enabled', False):
    actions['helm_gpg_key'] = {
        'command': 'mkdir -p /etc/apt/keyrings && curl -fsSL https://packages.buildkite.com/helm-linux/helm-debian/gpgkey | gpg --batch --yes --dearmor -o /etc/apt/keyrings/helm.gpg',
        'unless': 'test -f /etc/apt/keyrings/helm.gpg',
        'cascade_skip': False,
        'needed_by': ['action:apt_update'],
        'interactive': False,
    }
    files['/etc/apt/sources.list.d/helm.list'] = {
        'content': 'deb [arch=amd64 signed-by=/etc/apt/keyrings/helm.gpg] https://packages.buildkite.com/helm-linux/helm-debian/any/ any main\n',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'needs': ['action:helm_gpg_key'],
        'triggers': ['action:apt_update'],
    }
    pkg_apt['helm'] = {
        'installed': True,
    }
