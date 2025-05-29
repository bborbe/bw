if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
svc_systemd = {}

if node.metadata.get('docker', {}).get('enabled', False):
    svc_systemd['docker'] = {
        'running': node.metadata.get('docker', {}).get('enabled', False),
        'needs': ['pkg_apt:docker-ce'],
    }
    files['/etc/docker/daemon.json'] = {
        'source': 'daemon.json',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'needs': ['pkg_apt:docker-ce'],
        'triggers': [
            'svc_systemd:docker:restart',
        ],
    }
