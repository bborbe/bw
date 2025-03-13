@metadata_reactor.provides(
    'apt/repos',
)
def grafana_repo(metadata):
    if not metadata.get('telegraf', {}).get('enabled', False):
        return {}
    return {
        'apt': {
            'repos': {
                'telegraf': {
                    'installed': True,
                    'gpg_key': '05CE15085FC09D18E99EFB22684A14CF2582E0C5',
                    'sources': ['deb https://repos.influxdata.com/debian {} stable'.format(metadata.get('release', 'bullseye'))],
                },
            }
        }
    }
