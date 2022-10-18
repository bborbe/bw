files = {}
svc_systemd = {}
actions = {}

groups = {}
users = {}

if node.metadata.get('co2mon', {}).get('enabled', False):
    users['co2mon'] = {}
    groups['co2mon'] = {}

    actions['install_co2mon'] = {
        'command': 'virtualenv -p python3 /opt/co2mon/.env',
        'unless': 'test -d /opt/co2mon/.env',
        'needs': [
            'file:/opt/co2mon/requirements.txt',
            'pkg_apt:virtualenv',
            'pkg_apt:python3-pip',
        ],
        'triggers': ['action:install_co2mon_deps'],
    }
    actions['install_co2mon_deps'] = {
        'command': '/opt/co2mon/.env/bin/pip install -r /opt/co2mon/requirements.txt',
        'triggered': True,
        'triggers': [
            'svc_systemd:co2mon:restart',
        ],
    }
    files['/etc/udev/rules.d/90-co2mini.rules'] = {
        'source': '90-co2mini.rules',
        'content_type': 'text',
        'mode': '0444',
        'owner': 'root',
        'group': 'root',
        'triggers': [
            'svc_systemd:co2mon:restart',
        ],
    }
    files['/opt/co2mon/service.py'] = {
        'source': 'service.py',
        'content_type': 'text',
        'mode': '0555',
        'owner': 'root',
        'group': 'root',
        'triggers': [
            'svc_systemd:co2mon:restart',
        ],
    }
    files['/opt/co2mon/requirements.txt'] = {
        'source': 'requirements.txt',
        'content_type': 'text',
        'mode': '0444',
        'owner': 'root',
        'group': 'root',
        'triggers': [
            'action:install_co2mon_deps',
        ],
    }
    svc_systemd['co2mon'] = {
        'needs': [
            'file:/lib/systemd/system/co2mon.service',
            'file:/opt/co2mon/service.py',
            'action:install_co2mon',
            'user:co2mon',
            'group:co2mon',
        ],
    }
    files['/lib/systemd/system/co2mon.service'] = {
        'group': 'root',
        'mode': '0644',
        'needed_by': ['svc_systemd:co2mon'],
        'owner': 'root',
        'source': 'co2mon.service',
        'content_type': 'mako',
        'context': node.metadata.get('co2mon', {}),
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:co2mon:restart',
        ],
    }
else:
    users['co2mon'] = {
        'delete': True,
    }
    groups['co2mon'] = {
        'delete': True,
    }
    svc_systemd['co2mon'] = {
        'running': False,
        'enabled': False,
    }
    files['/etc/udev/rules.d/90-co2mini.rules'] = {
        'delete': True,
    }
    files['/opt/co2mon'] = {
        'delete': True,
    }
