@metadata_processor
def ntp_cron(metadata):
    metadata.setdefault('cron', {}).setdefault('jobs', {})
    metadata['cron']['jobs']['ntpdate'] = {
        'enabled': True,
        'schedule': '15 * * * *',
        'expression': 'ntpdate -s de.pool.ntp.org > /dev/null',
    }
    return metadata, DONE
