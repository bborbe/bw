def monit_filesystem(metadata):
    checks = metadata.setdefault('monit', {}).setdefault('checks', {})
    checks['filesystem'] = {
        'template': 'filesystem.conf',
    }
    return metadata


def monit_mailserver(metadata):
    if 'mailserver' in metadata.get('monit', {}):
        checks = metadata.setdefault('monit', {}).setdefault('checks', {})
        checks['mailserver'] = {
            'template': 'mailserver.conf',
            'context': {
                'recipient': metadata.get('monit', {}).get('mailserver', {}).get('recipient', ''),
                'sender': metadata.get('monit', {}).get('mailserver', {}).get('sender', ''),
                'server': metadata.get('monit', {}).get('mailserver', {}).get('server', ''),
                'port': metadata.get('monit', {}).get('mailserver', {}).get('port', ''),
                'username': metadata.get('monit', {}).get('mailserver', {}).get('username', ''),
                'password': metadata.get('monit', {}).get('mailserver', {}).get('password', ''),
            },
        }
    return metadata


def monit_httpchecks(metadata):
    checks = metadata.setdefault('monit', {}).setdefault('checks', {})
    for name, data in metadata.get('monit', {}).get('httpchecks', {}).items():
        checks['http_check_{name}'.format(name=name)] = {
            'enabled': data.get('enabled', True),
            'template': 'http_check.conf',
            'context': data,
        }
    return metadata


def monit_admin_password(metadata):
    metadata.setdefault('monit', {}).setdefault('password', repo.vault.password_for('monit admin {}'.format(node.name), length=16))
    return metadata