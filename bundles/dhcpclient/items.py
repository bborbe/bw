if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}

files = {}

files['/etc/dhcp/dhclient.conf'] = {
    'source': 'dhclient.conf',
    'content_type': 'text',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
    'context': {},
}

pkg_apt['dhcpcd5'] = {
    'installed': False,
}
