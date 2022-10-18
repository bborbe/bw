files = {}
svc_systemd = {}
actions = {}

groups = {}
users = {}
kernel_modules = {}

if node.metadata.get('bme280', {}).get('enabled', False):
    users['bme280'] = {
        'groups': ['i2c'],
    }
    groups['bme280'] = {}

    actions['install_bme280'] = {
        'command': 'virtualenv -p python3 /opt/bme280/.env',
        'unless': 'test -d /opt/bme280/.env',
        'needs': [
            'file:/opt/bme280/requirements.txt',
            'pkg_apt:virtualenv',
            'pkg_apt:python3-pip',
        ],
        'triggers': ['action:install_bme280_deps'],
    }
    actions['install_bme280_deps'] = {
        'command': '/opt/bme280/.env/bin/pip install -r /opt/bme280/requirements.txt',
        'triggered': True,
        'triggers': [
            'svc_systemd:bme280:restart',
        ],
    }
    actions['activate_i2c'] = {
        'command': 'raspi-config nonint do_i2c 0',
        'needs': [
            'pkg_apt:i2c-tools',
            'pkg_apt:python3-smbus',
        ],
    }
    files['/opt/bme280/service.py'] = {
        'source': 'service.py',
        'content_type': 'text',
        'mode': '0555',
        'owner': 'root',
        'group': 'root',
        'triggers': [
            'svc_systemd:bme280:restart',
        ],
    }
    files['/opt/bme280/requirements.txt'] = {
        'source': 'requirements.txt',
        'content_type': 'text',
        'mode': '0444',
        'owner': 'root',
        'group': 'root',
        'triggers': [
            'action:install_bme280_deps',
        ],
    }
    svc_systemd['bme280'] = {
        'needs': [
            'file:/lib/systemd/system/bme280.service',
            'file:/opt/bme280/service.py',
            'action:install_bme280',
            'user:bme280',
            'group:bme280',
        ],
    }
    files['/lib/systemd/system/bme280.service'] = {
        'group': 'root',
        'mode': '0644',
        'needed_by': ['svc_systemd:bme280'],
        'owner': 'root',
        'source': 'bme280.service',
        'content_type': 'mako',
        'context': node.metadata.get('bme280', {}),
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:bme280:restart',
        ],
    }
else:
    users['bme280'] = {
        'delete': True,
    }
    groups['bme280'] = {
        'delete': True,
    }
    svc_systemd['bme280'] = {
        'running': False,
        'enabled': False,
    }
    files['/opt/bme280'] = {
        'delete': True,
    }
