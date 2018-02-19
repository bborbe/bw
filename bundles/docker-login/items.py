import base64
import json

if node.os != 'ubuntu' and node.os != 'debian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
json_data = {}

if node.metadata.get('docker', {}).get('enabled', False):
    for domain, data in node.metadata.get('docker', {}).get('login', {}).items():
        username = data.get('username', '')
        if len(username) == 0:
            raise Exception('username empty for docker domain {domain}'.format(domain=domain))
        password = data.get('password', '')
        if len(password) == 0:
            raise Exception('password empty for docker domain {domain}'.format(domain=domain))
        auth = json_data.setdefault('auths', {}).setdefault(domain, {})
        auth['auth'] = base64.encodestring('{username}:{password}'.format(username=username, password=password).encode()).decode().replace('\n', '')

    files['/root/.docker/config.json'] = {
        'owner': 'root',
        'group': 'root',
        'mode': '0600',
        'content': json.dumps(json_data),
        'content_type': 'text',
        'needs': ['pkg_apt:docker-engine'],
    }
