directories = {}
files = {}
svc_systemd = {}

valheim = node.metadata.get('valheim', {})

if valheim.get('enabled', False):
    world_name = valheim.get('world_name', 'Valheim')
    # Deterministic, encrypted at rest in the repo's bw vault — the same pattern
    # bundles/monit and bundles/user use. No plaintext secret reaches git.
    server_password = repo.vault.password_for(
        'valheim server password {}'.format(node.name),
        length=20,
    )

    directories['/home/valheim/valheim'] = {
        'owner': 'valheim',
        'group': 'valheim',
        'mode': '0755',
        'needs': ['user:valheim'],
    }
    directories['/home/valheim/valheim/data'] = {
        'owner': 'valheim',
        'group': 'valheim',
        'mode': '0755',
        'needs': ['directory:/home/valheim/valheim'],
    }

    # 0600 owned by valheim: `docker compose` reads env_file client-side as the
    # invoking user (the unit runs as valheim), so a root-owned 0600 file would
    # be unreadable and `docker compose up` would fail.
    files['/home/valheim/valheim/valheim.env'] = {
        'content': (
            'SERVER_NAME={name}\n'
            'WORLD_NAME={name}\n'
            'SERVER_PASS={password}\n'
            'SERVER_PORT=2456\n'
        ).format(name=world_name, password=server_password),
        'owner': 'valheim',
        'group': 'valheim',
        'mode': '0600',
        'needs': ['directory:/home/valheim/valheim'],
        'triggers': ['svc_systemd:valheim:restart'],
    }
    files['/home/valheim/valheim/docker-compose.yml'] = {
        'source': 'docker-compose.yml',
        'owner': 'valheim',
        'group': 'valheim',
        'mode': '0644',
        'needs': ['directory:/home/valheim/valheim'],
        'triggers': ['svc_systemd:valheim:restart'],
    }

    files['/etc/sudoers.d/valheim-systemctl'] = {
        'source': 'valheim-systemctl',
        'owner': 'root',
        'group': 'root',
        'mode': '0440',
    }

    files['/lib/systemd/system/valheim.service'] = {
        'source': 'valheim.service',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'needed_by': ['svc_systemd:valheim'],
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:valheim:restart',
        ],
    }

    svc_systemd['valheim'] = {
        'needs': [
            'file:/lib/systemd/system/valheim.service',
            'file:/etc/sudoers.d/valheim-systemctl',
            'file:/home/valheim/valheim/docker-compose.yml',
            'file:/home/valheim/valheim/valheim.env',
            'directory:/home/valheim/valheim/data',
            'user:valheim',
            'pkg_apt:docker-ce',
        ],
    }
else:
    svc_systemd['valheim'] = {
        'running': False,
        'enabled': False,
    }
    files['/lib/systemd/system/valheim.service'] = {
        'delete': True,
    }
    files['/etc/sudoers.d/valheim-systemctl'] = {
        'delete': True,
    }
    files['/home/valheim/valheim/docker-compose.yml'] = {
        'delete': True,
    }
    files['/home/valheim/valheim/valheim.env'] = {
        'delete': True,
    }
