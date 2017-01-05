if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
directories = {}

dns_update = node.metadata.get('dns-update', {})
if dns_update.get('enabled', False):
    files['/usr/local/bin/dns-update.sh'] = {
        'source': 'dns-update.sh',
        'content_type': 'text',
        'owner': 'root',
        'group': 'root',
        'mode': '755',
    }
else:
    files['/usr/local/bin/dns-update.sh'] = {
        'delete': True,
    }

if dns_update.get('enabled', False):
    directories['/etc/dns-update/keys'] = {
        'mode': '0700',
        'owner': 'root',
        'group': 'root',
    }
    directories['/etc/dns-update'] = {
        'mode': '0700',
        'owner': 'root',
        'group': 'root',
    }
    for name, data in dns_update.get('updates', {}).items():
        files['/etc/dns-update/keys/{}.key'.format(name)] = {
            'content': data.get('key', ''),
            'owner': 'root',
            'group': 'root',
            'mode': '400',
        }
        files['/etc/dns-update/keys/{}.private'.format(name)] = {
            'content': data.get('private', ''),
            'owner': 'root',
            'group': 'root',
            'mode': '400',
        }
else:
    for name, data in dns_update.get('updates', {}).items():
        files['/etc/dns-update/keys/{}.key'.format(name)] = {
            'delete': True,
        }
        files['/etc/dns-update/keys/{}.private'.format(name)] = {
            'delete': True,
        }
