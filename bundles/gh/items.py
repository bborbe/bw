if not node.metadata.get('gh', {}).get('enabled', False):
    raise Exception('gh is not enabled for this node')

actions = {
    'gh_gpg_key': {
        'command': 'curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg -o /etc/apt/keyrings/gh.gpg',
        'unless': 'test -e /etc/apt/keyrings/gh.gpg',
        'cascade_skip': False,
        'needed_by': ['action:apt_update'],
    },
}

files = {
    '/etc/apt/sources.list.d/gh.list': {
        'content': 'deb [arch=amd64 signed-by=/etc/apt/keyrings/gh.gpg] https://cli.github.com/packages stable main\n',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'needs': ['action:gh_gpg_key'],
        'triggers': ['action:apt_update'],
    },
}

pkg_apt = {
    'gh': {},
}
