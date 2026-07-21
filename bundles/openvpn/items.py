from os.path import exists, expanduser, join

directories = {}
files = {}
svc_systemd = {}
pkg_apt = {}

openvpn_cfg = node.metadata.get('openvpn', {})

# PKI lives unencrypted in ~/.openvpn/hetzner/ on the operator laptop — exactly
# where the legacy world tool kept and read it (faithful refactoring; securing
# the storage is a tracked follow-up). Key/cert items are only declared when
# the local PKI is present, so an apply from a machine without it can never
# overwrite good key material on the node (it just skips those items).
PKI_DIR = expanduser('~/.openvpn/hetzner')


def local_pki(filename):
    with open(join(PKI_DIR, filename), 'r') as fh:
        return fh.read()


if openvpn_cfg.get('enabled', False):
    pkg_apt['openvpn'] = {
        'installed': True,
    }

    for path in (
        '/etc/openvpn/keys',
        '/var/log/openvpn',
    ):
        directories[path] = {
            'owner': 'root',
            'group': 'root',
            'mode': '0700',
        }

    # Intentionally NO purge: ccd still holds files for legacy/unmanaged
    # clients (e.g. nova — unidentified but actively connected) and for
    # decommissioned ones whose certs remain valid. Purging would silently
    # break nova's static IP; cleanup happens explicitly when each legacy
    # client is identified/decommissioned.
    directories['/etc/openvpn/ccd'] = {
        'owner': 'root',
        'group': 'root',
        'mode': '0700',
    }

    files['/etc/openvpn/server.conf'] = {
        'source': 'server.conf',
        'content_type': 'text',
        'owner': 'root',
        'group': 'root',
        'mode': '0600',
        'needs': ['pkg_apt:openvpn'],
        'triggers': ['svc_systemd:openvpn@server:restart'],
    }

    files['/etc/default/openvpn'] = {
        'source': 'openvpn.default',
        'content_type': 'text',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'needs': ['pkg_apt:openvpn'],
    }

    # copytruncate so the daemon keeps its open file handle — no signal/restart
    # needed on rotation. World never rotated this log at all.
    files['/etc/logrotate.d/openvpn'] = {
        'source': 'logrotate',
        'content_type': 'text',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
    }

    # Note: /etc/openvpn/ip_pool is deliberately NOT managed. It is
    # ifconfig-pool-persist runtime state that the openvpn daemon itself
    # rewrites; managing it would show permanent drift.

    for name, client in sorted(openvpn_cfg.get('clients', {}).items()):
        files['/etc/openvpn/ccd/' + name] = {
            'content': (
                'ifconfig-push {} 255.255.255.0\n'
                'iroute {} 255.255.255.255\n'
            ).format(client['vpn_ip'], client['lan_ip']),
            'owner': 'root',
            'group': 'root',
            'mode': '0600',
            'needs': ['directory:/etc/openvpn/ccd'],
            # ccd files are read per client connect — no server restart needed.
        }

    PKI_FILES = ('ca.crt', 'server.crt', 'server.key', 'dh.pem', 'ta.key')
    # All-or-nothing: only declare key items when the complete PKI set is
    # readable. A partial PKI (missing/unreadable file) must not abort the
    # items load nor deploy an incomplete key set — those items are simply
    # skipped, same as when PKI_DIR is absent entirely.
    if all(exists(join(PKI_DIR, f)) for f in PKI_FILES):
        for filename, mode in ((f, '0600') for f in PKI_FILES):
            files['/etc/openvpn/keys/' + filename] = {
                'content': local_pki(filename),
                'owner': 'root',
                'group': 'root',
                'mode': mode,
                'needs': ['directory:/etc/openvpn/keys'],
                'triggers': ['svc_systemd:openvpn@server:restart'],
            }

    # openvpn.service is the distro's oneshot sysv-compat aggregate (verified
    # live: `active (exited)`, single daemon process from openvpn@server) —
    # both units enabled matches the live/world state; no duplicate daemons.
    svc_systemd['openvpn'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:openvpn'],
    }
    svc_systemd['openvpn@server'] = {
        'running': True,
        'enabled': True,
        'needs': [
            'pkg_apt:openvpn',
            'file:/etc/openvpn/server.conf',
        ],
    }
