if node.os != 'ubuntu' and node.os != 'debian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}
svc_systemd = {}
actions = {}
files = {}
directories = {}

openhab_configs = (
    'html/habpanel-config.json',
    'items/default.items',
    'items/co2mon.items',
    'items/switches.items',
    'persistence/rrd4j.persist',
    'rules/co2alert.rules',
    'rules/default.rules',
    'rules/telegram.rules',
    'scripts/default.script',
    'services/addons.cfg',
    'services/mqtt.cfg',
    'services/mqtt-eventbus.cfg',
    'services/telegram.cfg',
    'sitemaps/default.sitemap',
    'things/default.things',
)

openhab_conf = '/etc/openhab2'
openhab_userdata = '/var/lib/openhab2'
openhab_log = '/var/log/openhab2'

openhab_directories = (
    '{}'.format(openhab_log),
    '{}'.format(openhab_userdata),
    '{}/tmp'.format(openhab_userdata),
    '{}/etc'.format(openhab_userdata),
    '{}'.format(openhab_conf),
)
openhab_directories_managed = (
    '{}/html'.format(openhab_conf),
    '{}/items'.format(openhab_conf),
    '{}/rules'.format(openhab_conf),
    '{}/persistence'.format(openhab_conf),
    '{}/scripts'.format(openhab_conf),
    '{}/services'.format(openhab_conf),
    '{}/sitemaps'.format(openhab_conf),
    '{}/things'.format(openhab_conf),
)

pkg_apt['openhab2'] = {
    'installed': node.metadata.get('openhab', {}).get('enabled', False),
}
pkg_apt['openjdk-8-jdk'] = {
    'installed': node.metadata.get('openhab', {}).get('enabled', False),
}

if node.metadata.get('openhab', {}).get('enabled', False):
    svc_systemd['openhab2'] = {
        'running': True,
        'enabled': True,
        'needs': [
            'user:openhab',
            'pkg_apt:openhab2',
            'pkg_apt:openjdk-8-jdk',
            'directory:{}'.format(openhab_conf),
            'directory:{}'.format(openhab_userdata),
        ],
    }
    for config in openhab_configs:
        files['{dir}/{file}'.format(dir=openhab_conf, file=config)] = {
            'source': config,
            'content_type': 'mako',
            'mode': '0644',
            'owner': 'openhab',
            'group': 'openhab',
            'context': node.metadata.get('openhab', {}),
            'needs': [
                'pkg_apt:openhab2',
            ],
            'triggers': [
                'svc_systemd:openhab2:restart',
            ],
        }
    for directory in openhab_directories:
        directories[directory] = {
            'mode': '0750',
            'owner': 'openhab',
            'group': 'openhab',
        }
    for directory in openhab_directories_managed:
        directories[directory] = {
            'mode': '0750',
            'owner': 'openhab',
            'group': 'openhab',
            'purge': True,
        }
else:
    svc_systemd['openhab2'] = {
        'running': False,
        'enabled': False,
    }
    for config in openhab_configs:
        files['{dir}/{file}'.format(dir=openhab_conf, file=config)] = {
            'delete': True,
        }
