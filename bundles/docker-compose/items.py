if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

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
