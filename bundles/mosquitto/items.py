if node.os != 'ubuntu' and node.os != 'debian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

actions = {}
files = {}
pkg_apt = {}
svc_systemd = {}
directories = {}

if node.metadata.get('mosquitto', {}).get('enabled', False):
    actions['update_mosquitto_passwd'] = {
        'command': 'mosquitto_passwd -U /etc/mosquitto/passwd',
        'triggers': ['svc_systemd:mosquitto:restart'],
        'needs': [
            'pkg_apt:mosquitto',
        ],
        'triggered': True,
    }
    files['/etc/mosquitto/passwd'] = {
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'content': '{}:{}'.format(
            node.metadata.get('mosquitto', {})['username'],
            node.metadata.get('mosquitto', {})['password'],
        ),
        'unless': 'grep "^{}:" /etc/mosquitto/passwd'.format(
            node.metadata.get('mosquitto', {})['username'],
        ),
        'triggers': ['action:update_mosquitto_passwd'],
    }
    pkg_apt['mosquitto'] = {
        'installed': True,
    }
    svc_systemd['mosquitto'] = {
        'running': True,
        'enabled': True,
        'needs': [
            'pkg_apt:mosquitto',
            'file:/etc/mosquitto/conf.d/auth.conf',
            'file:/etc/mosquitto/passwd',
        ],
    }
    directories['/etc/mosquitto/conf.d'] = {
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
        'purge': True,
    }
    files['/etc/mosquitto/conf.d/auth.conf'] = {
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'source': 'auth.conf',
        'triggers': ['svc_systemd:mosquitto:restart'],
    }
else:
    pkg_apt['mosquitto'] = {
        'installed': False,
    }
    svc_systemd['mosquitto'] = {
        'running': False,
        'enabled': False,
    }
    files['/etc/mosquitto/conf.d'] = {
        'delete': True,
    }
