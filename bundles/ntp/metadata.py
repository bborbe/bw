@metadata_reactor
def ntp_cron(metadata):
    return {
        'cron': {
            'jobs': {
                'ntpdate': {
                    'enabled': True,
                    'schedule': '15 * * * *',
                    'expression': 'ntpdate -s de.pool.ntp.org > /dev/null',
                }
            }
        }
    }
