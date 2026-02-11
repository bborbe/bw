if not node.metadata.get('gh', {}).get('enabled', False):
    raise Exception('gh is not enabled for this node')

pkg_apt = {
    'gh': {},
}
