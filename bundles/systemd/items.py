os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

actions = {
    'systemd-reload': {
        'command': 'systemctl daemon-reload',
        'triggered': True,
    },
}
