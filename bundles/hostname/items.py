if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}

actions = {}

parts = node.hostname.split('.', 1)
if len(parts) != 2:
    raise Exception('invalid hostname {}'.format(node.hostname))

name = parts[0]

actions['set_hostname_{}'.format(name)] = {
    'command': 'hostnamectl set-hostname {}'.format(name),
    'triggered': True,
    'cascade_skip': False,
}

files['/etc/hostname'] = {
    'source': 'hostname',
    'content_type': 'mako',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
    'context': {
        'hostname': name,
    },
    'triggers': ['action:set_hostname_{}'.format(name)],
}

hosts_v4 = node.metadata.get('hosts', {}).get('ipv4', {})
if len(hosts_v4) == 0:
    hosts_v4['127.0.0.1'] = [node.hostname, name]
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
