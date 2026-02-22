@metadata_reactor
def monit_filesystem(metadata):
    return {
        'monit': {
            'checks': {
                'filesystem': {
                    'template': 'filesystem.conf',
                },
            }
        },
    }

@metadata_reactor
def monit_mailserver(metadata):
    if 'mailserver' in metadata.get('monit', {}):
        return {
            'monit': {
                'checks': {
                    'mailserver': {
                        'template': 'mailserver.conf',
                        'context': {
                            'recipient': metadata.get('monit', {}).get('mailserver', {}).get('recipient', ''),
                            'sender': metadata.get('monit', {}).get('mailserver', {}).get('sender', ''),
                            'server': metadata.get('monit', {}).get('mailserver', {}).get('server', ''),
                            'port': metadata.get('monit', {}).get('mailserver', {}).get('port', ''),
                            'username': metadata.get('monit', {}).get('mailserver', {}).get('username', ''),
                            'password': metadata.get('monit', {}).get('mailserver', {}).get('password', ''),
                        },
                    },
                },
            },
        }
    return {}


@metadata_reactor
def monit_httpchecks(metadata):
    result = {
        'monit': {
            'checks': {
            },
        },
    }
    for name, data in metadata.get('monit', {}).get('httpchecks', {}).items():
        result['http_check_{name}'.format(name=name)] = {
            'enabled': data.get('enabled', True),
            'template': 'http_check.conf',
            'context': data,
        }
    return result


@metadata_reactor
def monit_admin_password(metadata):
    return {
        'monit': {
            'password': repo.vault.password_for('monit admin {}'.format(node.name), length=16),
        },
    }


@metadata_reactor
def monit_test_alert(metadata):
    if metadata.get('monit', {}).get('test_alert', False):
        return {
            'monit': {
                'checks': {
                    'test-alert': {
                        'template': 'test-alert.conf',
                    },
                },
            },
        }
    return {}
