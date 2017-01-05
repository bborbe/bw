if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

actions = {}

if node.metadata.get('docker', {}).get('enabled', False):
    for host, data in node.metadata.get('docker', {}).get('login', {}).items():
        actions['docker_login'] = {
            # TODO: handle password change
            'unless': 'test -f /root/.docker/config.json',
            'command': "su -c 'docker login {host} -u {username} -p {password}'".format(
                host=host,
                username=data.get('username', ''),
                password=data.get('password', ''),
            ),
            'needs': ['pkg_apt:docker-engine'],
        }
