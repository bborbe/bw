if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}
svc_systemd = {}
actions = {}
files = {}



if node.metadata.get('openhab', {}).get('enabled', False):
    svc_systemd['openhab'] = {
        'running': True,
        'enabled': True,
        'needs': [
            'action:install_openhab',
            'user:openhab',
            'pkg_apt:openjdk-8-jdk',
            'file:/etc/systemd/system/openhab.service',
        ],
    }
    actions['install_openhab'] = {
        'command': (
            'cd /opt && '
            'curl --connect-timeout 10 --max-time 30 -sSLo openhab.zip https://bintray.com/openhab/mvn/download_file?file_path=org%2Fopenhab%2Fdistro%2Fopenhab%2F{version}%2Fopenhab-{version}.zip && '
            'unzip openhab.zip -d openhab && '
            'rm -f openhab.zip'
        ).format(version=node.metadata['openhab'].get('version', '2.2.0')),
        'unless': 'test -d /opt/openhab',
        'needs': [
            'pkg_apt:unzip',
            'pkg_apt:curl',
        ],
        'cascade_skip': False,
    }
    files['/etc/systemd/system/openhab.service'] = {
        'source': 'openhab.service',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {},
        'triggers': [
            'svc_systemd:openhab:restart',
            'action:systemd-reload',
        ],
    }

else:
    svc_systemd['openhab'] = {
        'running': False,
        'enabled': False,
    }
    files['/opt/openhab'] = {
        'delete': True,
    }
    files['/etc/systemd/system/openhab.service'] = {
        'delete': True,
    }
