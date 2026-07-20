directories = {}
files = {}
svc_systemd = {}

poste = node.metadata.get('poste', {})

if poste.get('enabled', False):
    # Mail data volume (mailboxes + config). Only the mount-point node is managed
    # here (non-recursive, no purge) — the poste.io container owns /data's contents.
    directories['/data/poste'] = {
        'owner': 'root',
        'group': 'root',
        'mode': '0755',
    }
    # Container env (HTTPS off, clamav off). No secrets — plain file, kept outside
    # the /data/poste volume so it isn't exposed inside the container.
    files['/home/poste.environment'] = {
        'source': 'environment',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'triggers': ['svc_systemd:poste:restart'],
    }
    # Remove the legacy world-managed unit at /etc/systemd/system/, which shadows
    # this bundle's /lib unit (systemd prefers /etc). Left behind by the old
    # `world` tool; deleting it makes bw's unit authoritative.
    files['/etc/systemd/system/poste.service'] = {
        'delete': True,
    }
    files['/lib/systemd/system/poste.service'] = {
        'source': 'poste.service',
        'content_type': 'mako',
        'context': poste,
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'needed_by': ['svc_systemd:poste'],
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:poste:restart',
        ],
    }
    svc_systemd['poste'] = {
        'needs': [
            'file:/lib/systemd/system/poste.service',
            'file:/home/poste.environment',
            'directory:/data/poste',
        ],
    }
    # poste binds host :25 — the host's postfix MTA must not hold that port.
    # world did this via DisablePostfix (ServiceStop); replicate by ensuring
    # postfix stays stopped + disabled.
    svc_systemd['postfix'] = {
        'running': False,
        'enabled': False,
    }
else:
    svc_systemd['poste'] = {
        'running': False,
        'enabled': False,
    }
    files['/lib/systemd/system/poste.service'] = {
        'delete': True,
    }
    files['/etc/systemd/system/poste.service'] = {
        'delete': True,
    }
    files['/home/poste.environment'] = {
        'delete': True,
    }
