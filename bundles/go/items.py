directories = {}
actions = {}
files = {}

if node.metadata.get('go', {}).get('enabled', False):
    directories['/opt/go'] = {
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
    }

    actions['install_golang'] = {
        'command': 'rm -rf /opt/go/* && curl -Ls "https://dl.google.com/go/go{version}.{os}-{arch}.tar.gz" | tar -xz --directory "/opt/go" --strip-components=1 --no-same-owner'.format(
            version=node.metadata['go']['version'],
            os=node.metadata['go']['os'],
            arch=node.metadata['go']['arch'],
        ),
        'unless': 'sh -c \'test -x /opt/go/bin/go && test "$(/opt/go/bin/go version)" = "go version go{version} {os}/{arch}"\''.format(
            version=node.metadata['go']['version'],
            os=node.metadata['go']['os'],
            arch=node.metadata['go']['arch'],
        ),
        'needs': [
            'pkg_apt:curl',
        ],
    }
else:
    files['/opt/go'] = {
        'delete': True,
    }
