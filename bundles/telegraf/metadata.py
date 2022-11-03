@metadata_reactor
def grafana_repo(metadata):
    if metadata.get('telegraf', {}).get('enabled', False):
        return {
            'apt': {
                'repos': {
                    'telegraf': {
                        'installed': True,
                        'gpg_key': '05CE15085FC09D18E99EFB22684A14CF2582E0C5',
                        'sources': ['deb https://repos.influxdata.com/debian bullseye stable'],
                    },
                }
            }
        }
    else:
        return {}

