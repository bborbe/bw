if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}
svc_systemd = {}

if node.metadata.get('influxdb', {}).get('enabled', False):
    pkg_apt['influxdb'] = {
        'installed': True,
    }
    svc_systemd['influxdb'] = {
        'running': True,
        'enabled': True,
    }    
else:
    pkg_apt['influxdb'] = {
        'installed': False,
    }
    svc_systemd['influxdb'] = {
        'running': False,
        'enabled': False,
    }