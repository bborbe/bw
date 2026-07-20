directories = {}
files = {}
svc_systemd = {}

bind = node.metadata.get('bind', {})

if bind.get('enabled', False):
    # Zone data volume (bind-mounted as both /etc/bind and /var/lib/bind in the
    # container). Only the mount-point node is managed (non-recursive, no purge)
    # — named owns the contents (zone files, journals, keys). Perms match the
    # live state world left behind (root:root 0777; named writes journals as the
    # container's 'bind' user, so the dir must stay group/other-writable unless
    # ownership is reworked — out of scope for the faithful migration).
    directories['/data/bind'] = {
        'owner': 'root',
        'group': 'root',
        'mode': '0777',
    }
    # Remove the legacy world-managed unit at /etc/systemd/system/, which shadows
    # this bundle's /lib unit (systemd prefers /etc). Left behind by the old
    # `world` tool; deleting it makes bw's unit authoritative.
    files['/etc/systemd/system/bind.service'] = {
        'delete': True,
    }
    files['/lib/systemd/system/bind.service'] = {
        'source': 'bind.service',
        'content_type': 'mako',
        'context': bind,
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'needed_by': ['svc_systemd:bind'],
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:bind:restart',
        ],
    }
    svc_systemd['bind'] = {
        'needs': [
            'file:/lib/systemd/system/bind.service',
            'directory:/data/bind',
        ],
    }
else:
    svc_systemd['bind'] = {
        'running': False,
        'enabled': False,
    }
    files['/lib/systemd/system/bind.service'] = {
        'delete': True,
    }
    files['/etc/systemd/system/bind.service'] = {
        'delete': True,
    }
