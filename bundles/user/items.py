os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

for username, data in node.metadata['users'].items():
    homedir = data.get('home', '/home/{}'.format(username))
    directories = {
        homedir: {
            'mode': '0700',
            'owner': username,
            'group': username,
        },
    }
