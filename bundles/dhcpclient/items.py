if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {
    '/etc/dhcp/dhclient.conf': {
        'source': 'dhclient.conf',
        'content_type': 'text',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {},
    },
}
