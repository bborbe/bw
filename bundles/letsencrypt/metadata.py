def letsencrypt_checkout(metadata):
    if metadata.get('letsencrypt', {}).get('enabled', False):
        metadata.setdefault('git', {}).setdefault('clones', {})
        metadata['git']['clones']['letsencrypt-app'] = {
            'branch': 'master',
            'repo': 'https://github.com/bborbe/letsencrypt.sh.git',
            'target': '/opt/letsencrypt.sh',
        }
        config_repo = metadata.get('letsencrypt', {}).get('config_repo', {}).get('repo', '')
        if len(config_repo) == 0:
            raise Exception('letsencrytp config repo missing')
        metadata['git']['clones']['letsencrypt-cfg'] = {
            'branch': metadata.get('letsencrypt', {}).get('config_repo', {}).get('branch', 'master'),
            'repo': config_repo,
            'target': '/etc/letsencrypt.sh',
        }
    return metadata
