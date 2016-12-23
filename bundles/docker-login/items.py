os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

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
