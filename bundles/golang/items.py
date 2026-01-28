directories = {}
actions = {}
files = {}

default_golang_version = '1.25.6'

if node.metadata.get('golang', {}).get('enabled', False):
    directories['/opt/go'] = {
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
    }

    version = node.metadata['golang'].get('version', default_golang_version)
    os = node.metadata['golang']['os']
    arch = node.metadata['golang']['arch']
    actions['install_golang'] = {
        'command': 'rm -rf /opt/go/* && curl -Ls "https://dl.google.com/go/go{version}.{os}-{arch}.tar.gz" | tar -xz --directory "/opt/go" --strip-components=1 --no-same-owner'.format(
            version=version,
            os=os,
            arch=arch,
        ),
        'unless': 'sh -c \'test -x /opt/go/bin/go && test "$(/opt/go/bin/go version)" = "go version go{version} {os}/{arch}"\''.format(
            version=version,
            os=os,
            arch=arch,
        ),
        'needs': [
            'pkg_apt:curl',
        ],
    }
else:
    files['/opt/go'] = {
        'delete': True,
    }
