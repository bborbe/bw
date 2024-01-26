if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}
svc_systemd = {}
files = {}

if node.metadata.get('docker-registry', {}).get('enabled', False):
    pkg_apt['docker-registry'] = {
        'installed': True,
    }
    files['/etc/docker/registry/config.yml'] = {
        'source': 'config.yml',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
    }
else:
    pkg_apt['docker-registry'] = {
        'installed': False,
    }

    files['/etc/docker/registry/config.yml'] = {
        'delete': True,
    }
