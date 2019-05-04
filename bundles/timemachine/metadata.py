import bwtv as teamvault

@metadata_processor
def timemachine_users(metadata):
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
            data = metadata.setdefault('users', {})
            data[username]['enabled'] = True
            data[username]['home'] = path
            data[username]['shell'] = '/bin/false'
            data[username]['password'] = password
            data[username]['salt'] = 'w9AVl6dZcq4i3Q3d'
    else:
        for username, data in metadata.get('timemachine', {}).get('users', {}).items():
            metadata.setdefault('users', {})[username] = {
                'enabled': False,
            }
    return metadata, DONE
