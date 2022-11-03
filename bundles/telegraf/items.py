if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(
        node.os, node.os_version))

pkg_apt = {}
svc_systemd = {}
files = {}

if node.metadata.get('telegraf', {}).get('enabled', False):
    pkg_apt['telegraf'] = {
        'installed': True,
        'needs': ['file:/etc/apt/sources.list.d/telegraf.list'],
    }
    svc_systemd['telegraf'] = {
        'running': True,
        'enabled': True,
    }    
    files['/etc/telegraf/telegraf.d/mqtt.conf'] = {
        'source': 'mqtt.conf',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'mqtt_server': 'tcp://localhost:1883',
            'mqtt_username': node.metadata.get('mosquitto', {})['username'],
            'mqtt_password': node.metadata.get('mosquitto', {})['password'],
        },
        'needs': ['pkg_apt:telegraf'],
        'triggers': ['svc_systemd:telegraf:restart'],
    }
else:
    svc_systemd['telegraf'] = {
        'running': False,
        'enabled': False,
    }    
    pkg_apt['telegraf'] = {
        'installed': False,
    }
