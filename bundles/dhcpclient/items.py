os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

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
