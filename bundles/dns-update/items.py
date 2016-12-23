os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

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
    directories['/etc/dns-update'] = {
        'delete': True,
    }
