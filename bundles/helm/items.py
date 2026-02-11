if not node.metadata.get('helm', {}).get('enabled', False):
    raise Exception('helm is not enabled for this node')

actions = {
    'helm_gpg_key': {
        'command': 'curl -fsSL https://packages.buildkite.com/helm-linux/helm-debian/gpgkey | gpg --dearmor -o /etc/apt/keyrings/helm.gpg',
        'unless': 'apt-key --keyring /etc/apt/keyrings/helm.gpg list 2>/dev/null | grep -q 4B196BE9C4313D06',
        'cascade_skip': False,
        'needed_by': ['action:apt_update'],
    },
}

files = {
    '/etc/apt/sources.list.d/helm.list': {
        'content': 'deb [arch=amd64 signed-by=/etc/apt/keyrings/helm.gpg] https://packages.buildkite.com/helm-linux/helm-debian/any/ any main\n',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'needs': ['action:helm_gpg_key'],
        'triggers': ['action:apt_update'],
    },
}

pkg_apt = {
    'helm': {},
}
