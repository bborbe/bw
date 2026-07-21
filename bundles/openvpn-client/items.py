from os.path import exists, expanduser, join

directories = {}
files = {}
svc_systemd = {}
pkg_apt = {}

client_cfg = node.metadata.get('openvpn-client', {})

# Per-client PKI lives unencrypted in ~/.openvpn/<name>/ on the operator
# laptop — exactly where the legacy world tool kept and read it (faithful
# refactoring; securing the storage is a tracked follow-up). Key/cert items
# are only declared when the complete local PKI is present, so an apply from
# a machine without it can never overwrite key material on the node.
PKI_FILES = ('ca.crt', 'client.crt', 'client.key', 'ta.key')


def local_pki(pki_dir, filename):
    path = join(pki_dir, filename)
    try:
        with open(path, 'r') as fh:
            return fh.read()
    except OSError as exc:
        raise Exception(
            'openvpn-client: cannot read PKI file {} ({}) — fix the local '
            'PKI before applying'.format(path, exc)
        )


if client_cfg.get('enabled', False):
    client_name = client_cfg.get('name')
    if not client_name:
        raise Exception(
            'openvpn-client enabled on {} but no name set'.format(node.name)
        )

    pkg_apt['openvpn'] = {
        'installed': True,
    }

    directories['/etc/openvpn'] = {
        'owner': 'root',
        'group': 'root',
        'mode': '0700',
    }

    files['/etc/openvpn/client.conf'] = {
        'source': 'client.conf',
        'content_type': 'text',
        'owner': 'root',
        'group': 'root',
        'mode': '0600',
        'needs': ['pkg_apt:openvpn'],
        'triggers': ['svc_systemd:openvpn@client:restart'],
    }

    files['/etc/default/openvpn'] = {
        'source': 'openvpn.default',
        'content_type': 'text',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'needs': ['pkg_apt:openvpn'],
    }

    pki_dir = expanduser(join('~/.openvpn', client_name))
    # PKI dir absent entirely = not the operator laptop (CI, other machines):
    # key items are skipped silently. Present but INCOMPLETE = broken local
    # PKI: fail loudly instead of silently deploying a partial key set.
    if exists(pki_dir):
        missing = [f for f in PKI_FILES if not exists(join(pki_dir, f))]
        if missing:
            raise Exception(
                'openvpn-client: incomplete PKI in {} — missing: {}'.format(
                    pki_dir, ', '.join(missing)
                )
            )
        for filename in PKI_FILES:
            files['/etc/openvpn/' + filename] = {
                'content': local_pki(pki_dir, filename),
                'owner': 'root',
                'group': 'root',
                'mode': '0600',
                'needs': ['directory:/etc/openvpn'],
                'triggers': ['svc_systemd:openvpn@client:restart'],
            }

    # openvpn.service is the distro's oneshot sysv-compat aggregate — both
    # units enabled matches the live/world state; single daemon process.
    svc_systemd['openvpn'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:openvpn'],
    }
    svc_systemd['openvpn@client'] = {
        'running': True,
        'enabled': True,
        'needs': [
            'pkg_apt:openvpn',
            'file:/etc/openvpn/client.conf',
        ],
    }
