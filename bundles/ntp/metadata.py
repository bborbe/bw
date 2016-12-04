def ntp_cron(metadata):
    metadata.setdefault('cron', {}).setdefault('jobs', {})
    metadata['cron']['jobs']['ntpdate'] = '15 * * * * root ntpdate -s de.pool.ntp.org > /dev/null'
    return metadata
