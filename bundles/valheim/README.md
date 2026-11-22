# valheim

Runs a Valheim dedicated server as an unprivileged service user.

## What it manages

| Path | Owner | Purpose |
|---|---|---|
| `/home/valheim/valheim` | `valheim:valheim` | working directory |
| `/home/valheim/valheim/docker-compose.yml` | `valheim:valheim` | the stack (lloesche/valheim-server) |
| `/home/valheim/valheim/valheim.env` | `valheim:valheim` 0600 | world name + generated password |
| `/home/valheim/valheim/data` | `valheim:valheim` | world save (`/config` in the container) |
| `/lib/systemd/system/valheim.service` | `root:root` | `docker compose up -d` as `valheim` |
| `/etc/sudoers.d/valheim-systemctl` | `root:root` 0440 | narrow systemctl grant |

## Notes

- **The image is pinned, and `ExecStop` is `docker compose stop`, not `down`.** The
  Valheim server install lives at `/opt/valheim` *inside the container* (~4 GB), not on
  the bind mount — only `/config` is persisted. Removing the container therefore makes
  the next start re-download everything from Steam. `stop` keeps the container, so a
  service restart is instant; a `docker compose down`, an image bump, or a container
  recreate still triggers one full download.
- **`server_name` and `world_name` are separate.** `server_name` is the label in the
  server browser (`SERVER_NAME`); `world_name` is the save directory under
  `data/worlds_local/` (`WORLD_NAME`). Renaming the server is safe at any time;
  changing `world_name` starts a new world and orphans the old save.
- **The world password lives in TeamVault,** not in git and not in the repo vault.
  `nodes/hz.hetzner-2.py` resolves `teamvault.password('eOBZ4O', site='benjamin-borbe')`
  and `files/valheim.env` renders it as a mako template. `repo.vault.password_for` is
  deliberately not used: it resolves eagerly and breaks `bw test` in CI, where the
  vault's `generate` key is absent. Read the password with
  `teamvault-cli password eOBZ4O` or on the host with
  `sudo cat /home/valheim/valheim/valheim.env`.
- **`/usr/bin/systemctl`, never `/bin/systemctl`,** in the sudoers drop-in: sudo does
  not follow noble's `/bin -> /usr/bin` symlink, so a `/bin/` path silently never matches.
- **No iptables rule is needed for the game ports.** With `-p 2456-2457:2456-2457/udp`
  the packets traverse `nat PREROUTING` DNAT → `FORWARD` → the `DOCKER` chain, never
  `INPUT`. The host's `INPUT DROP` policy does not gate published container ports; the
  iptables bundle's `docker-iptables-reconcile` action restores Docker's chains after
  each apply.
- `enabled: False` deletes the unit, the sudoers drop-in, the compose file and the env
  file — but **not** `/home/valheim/valheim/data`, so a disable never destroys a world.
