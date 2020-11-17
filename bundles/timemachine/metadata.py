import bwtv as teamvault


@metadata_reactor
def timemachine_users(metadata):
    result = {
        'users': {}
    }
    if metadata.get('timemachine', {}).get('enabled', False):
        for username, data in metadata.get('timemachine', {}).get('users', {}).items():
            path = data.get('path', '')
            if len(path) == 0:
                raise Exception('path missing')
            if 'password_hash' in data:
                password = teamvault.password(data['password_hash'], site='benjamin-borbe')
            else:
                password = data.get('password', '')
            if len(password) == 0:
                raise Exception('password missing')
            result['users'][username] = {
                'enabled': True,
                'home': path,
                'shell': '/bin/false',
                'password': password,
                'salt': 'w9AVl6dZcq4i3Q3d',
            }
    return result


@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('timemachine', {}).get('enabled', False):
        # allow netatalk
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 548 -j ACCEPT')
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
