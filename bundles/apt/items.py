if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {
    'apt-transport-https': {},
    'aptitude': {},
}

actions = {}

files = {}

actions['apt_update'] = {
    'command': 'apt-get update',
    'needed_by': ['pkg_apt:'],
    'triggered': True,
    'cascade_skip': False,
}

if node.metadata.get('os') == 'ubuntu' and node.metadata.get('release'):
    files['/etc/apt/sources.list'] = {
        'source': 'source.list',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'lines': [
                'deb     http://ftp.uni-stuttgart.de/ubuntu {}-backports main restricted universe multiverse'.format(node.metadata.get('release')),
                'deb-src http://ftp.uni-stuttgart.de/ubuntu {}-backports main restricted universe multiverse'.format(node.metadata.get('release')),
                'deb     http://ftp.uni-stuttgart.de/ubuntu {} main restricted'.format(node.metadata.get('release')),
                'deb-src http://ftp.uni-stuttgart.de/ubuntu {} main restricted'.format(node.metadata.get('release')),
                'deb     http://ftp.uni-stuttgart.de/ubuntu {} multiverse'.format(node.metadata.get('release')),
                'deb-src http://ftp.uni-stuttgart.de/ubuntu {} multiverse'.format(node.metadata.get('release')),
                'deb     http://ftp.uni-stuttgart.de/ubuntu {} universe'.format(node.metadata.get('release')),
                'deb-src http://ftp.uni-stuttgart.de/ubuntu {} universe'.format(node.metadata.get('release')),
                'deb     http://ftp.uni-stuttgart.de/ubuntu {}-updates main restricted'.format(node.metadata.get('release')),
                'deb-src http://ftp.uni-stuttgart.de/ubuntu {}-updates main restricted'.format(node.metadata.get('release')),
                'deb     http://ftp.uni-stuttgart.de/ubuntu {}-updates multiverse'.format(node.metadata.get('release')),
                'deb-src http://ftp.uni-stuttgart.de/ubuntu {}-updates multiverse'.format(node.metadata.get('release')),
                'deb     http://ftp.uni-stuttgart.de/ubuntu {}-updates universe'.format(node.metadata.get('release')),
                'deb-src http://ftp.uni-stuttgart.de/ubuntu {}-updates universe'.format(node.metadata.get('release')),
                'deb     http://security.ubuntu.com/ubuntu {}-security main restricted'.format(node.metadata.get('release')),
                'deb-src http://security.ubuntu.com/ubuntu {}-security main restricted'.format(node.metadata.get('release')),
                'deb     http://security.ubuntu.com/ubuntu {}-security multiverse'.format(node.metadata.get('release')),
                'deb-src http://security.ubuntu.com/ubuntu {}-security multiverse'.format(node.metadata.get('release')),
                'deb     http://security.ubuntu.com/ubuntu {}-security universe'.format(node.metadata.get('release')),
                'deb-src http://security.ubuntu.com/ubuntu {}-security universe'.format(node.metadata.get('release')),
            ],
        },
        'triggers': ['action:apt_update'],
    }
if node.metadata.get('os') == 'raspbian' and node.metadata.get('release'):
    files['/etc/apt/sources.list'] = {
        'source': 'source.list',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'lines': [
                'deb http://raspbian.raspberrypi.org/raspbian/ {} main contrib non-free rpi'.format(node.metadata.get('release')),
                '#deb-src http://raspbian.raspberrypi.org/raspbian/ {} main contrib non-free rpi'.format(node.metadata.get('release')),
            ],
        },
        'triggers': ['action:apt_update'],
    }

for name, data in node.metadata.get('apt', {}).get('repos', {}).items():
    if data['installed']:
        actions['add_gpg_key_{}'.format(data['gpg_key'])] = {
            'command': 'apt-key adv --keyserver keyserver.ubuntu.com --recv-keys {}'.format(data['gpg_key']),
            'unless': 'apt-key list | tr -d "[:blank:]" | grep {}'.format(data['gpg_key']),
            'cascade_skip': False,
            'needed_by': ['action:apt_update'],
        }
        files['/etc/apt/sources.list.d/{}.list'.format(name)] = {
            'source': 'source.list',
            'content_type': 'mako',
            'mode': '0644',
            'owner': 'root',
            'group': 'root',
            'context': {
                'lines': data['sources'],
            },
            'needs': ['action:add_gpg_key_{}'.format(data['gpg_key'])],
            'triggers': ['action:apt_update'],
        }
    else:
        files['/etc/apt/sources.list.d/{}.list'.format(name)] = {
            'delete': not data['installed'],
            'triggers': ['action:apt_update'],
        }

for name, data in node.metadata.get('apt', {}).get('packages', {}).items():
    pkg_apt[name] = data
