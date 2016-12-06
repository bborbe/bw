def letsencrypt_checkout(metadata):
    if metadata.get('letsencrypt', {}).get('enabled', False):
        metadata.setdefault('git', {}).setdefault('clones', {})
        metadata['git']['clones']['letsencrypt-app'] = {
            'branch': 'master',
            'repo': 'https://github.com/bborbe/letsencrypt.sh.git',
            'target': '/opt/letsencrypt.sh',
        }
    return metadata
