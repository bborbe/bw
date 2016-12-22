os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

if node.metadata.get('docker', {}).get('enabled', False):
    actions = {
        'chmod_docker_compose': {
            'command': 'chmod a+x /usr/local/bin/docker-compose',
            'triggered': True,
        },
        'install_docker_compose': {
            'unless': 'test -e /usr/local/bin/docker-compose',
            'command': 'curl -Lso /usr/local/bin/docker-compose https://github.com/docker/compose/releases/download/1.8.1/run.sh',
            'triggers': [
                'action:chmod_docker_compose',
            ],
        },
    }
