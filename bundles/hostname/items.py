os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

parts = node.hostname.split('.', 1)
if len(parts) != 2:
    raise Exception('invalid hostname {}'.format(node.hostname))

files = {}

files['/etc/hostname'] = {
    'source': 'hostname',
    'content_type': 'mako',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
    'context': {
        'hostname': parts[0],
    },
}

hosts_v4 = node.metadata.get('hosts', {}).get('ipv4', {})
if len(hosts_v4) == 0:
    hosts_v4['127.0.0.1'] = [node.hostname, parts[0]]
hosts_v6 = node.metadata.get('hosts', {}).get('ipv6', {})

files['/etc/hosts'] = {
    'source': 'hosts',
    'content_type': 'mako',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
    'context': {
        'ipv4': hosts_v4,
        'ipv6': hosts_v6,
    },
}
