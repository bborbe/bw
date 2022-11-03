if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}
svc_systemd = {}

if node.metadata.get('grafana', {}).get('enabled', False):
    pkg_apt['grafana'] = {
        'installed': True,
        'needs': ['file:/etc/apt/sources.list.d/grafana.list'],
    }
    svc_systemd['grafana-server'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:grafana'],
    }    
else:
    pkg_apt['grafana'] = {
        'installed': False,
    }
    svc_systemd['grafana-server'] = {
        'running': False,
        'enabled': False,
    }