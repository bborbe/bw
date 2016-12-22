import bwtv as teamvault

os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

if node.metadata.get('docker', {}).get('enabled', False):
    actions = {
        'docker_login': {
            # TODO: handle password change
            'unless': 'test -f /root/.docker/config.json',
            'command': "su -c 'docker login docker.tools.seibert-media.net -u {} -p {}'".format(teamvault.username('7qGQOW', site='benjamin-borbe'), teamvault.password('7qGQOW', site='benjamin-borbe')),
            'needs': ['pkg_apt:docker-engine'],
        },
    }
