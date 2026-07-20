# poste

Deploys [Poste.io](https://poste.io/) — a self-hosted all-in-one mail server
(SMTP/IMAP/POP3 + webmail admin) — as a Docker container under a systemd unit,
fronted by the nginx `mail.benjamin-borbe.de` vhost (proxies the admin UI on
`localhost:8001`).

Migrated from the legacy `world` tool (`configuration/service/poste.go`).

## Image

`bborbe/poste.io:{vendor}-{wrapper}` (e.g. `2.5.13-2.0.1`) — a **custom** image
built from [`github.com/bborbe/poste.io`](https://github.com/bborbe/poste.io):
`FROM analogic/poste.io:<vendor>` plus POP3 enabled in dovecot and clamd turned
off. **Not** the public `analogic/poste.io` image. Published via the repo's own
`make build upload` (house pattern) — world no longer builds it.

## Metadata

```python
'poste': {
    'enabled': True,
    'version': '2.5.13-2.0.1',  # bborbe/poste.io image tag
    'admin_port': 8001,         # host port -> container :80 (nginx 'mail' vhost proxies this)
},
```

## Files rendered

- `/home/poste.environment` — `HTTPS=OFF`, `DISABLE_CLAMAV=TRUE` (plain, no secrets)
- `/lib/systemd/system/poste.service` — docker-run unit (explicit `-p` port maps, `--env-file`, `/data/poste:/data`)

## Data

- `/data/poste` (host) → `/data` (container) — mailboxes + config. Non-recursive
  mount-point management only; the container owns the contents.

## Ports (opened via the iptables reactor)

- `25/tcp` SMTP, `465/tcp` SMTPS, `587/tcp` submission, `993/tcp` IMAPS
- admin `8001/tcp` → container `:80` (behind the nginx `mail` vhost; not opened directly)

## Host prep

- Host `postfix` is stopped + disabled so poste can bind `:25` (replaces world's `DisablePostfix`).

## Enabled on

- `hz.hetzner-1`
