import bwtv as teamvault

os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

if node.metadata.get('docker', False):
    actions = {
        'docker_login': {
            # TODO: handle password change
            'unless': 'test -f /root/.docker/config.json',
            'command': "su -c 'docker login docker.tools.seibert-media.net -u {} -p {}'".format(teamvault.username('7qGQOW'), teamvault.password("7qGQOW")),
            'needs': ['pkg_apt:docker.io'],
        },
    }
