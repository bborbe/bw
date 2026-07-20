# screego

Deploys [screego](https://screego.net/) — a self-hosted screen-sharing server —
as a Docker container under a systemd unit (host networking for its TURN server),
fronted by an nginx websocket vhost (e.g. `screen.benjamin-borbe.de`).

Migrated from the legacy `world` tool (`configuration/service/screego.go`).

## Metadata

```python
'screego': {
    'enabled': True,
    'version': '1.12.4',            # bborbe/screego image tag
    'external_ip': '159.69.203.89', # SCREEGO_EXTERNAL_IP (node public IP)
    'secret': teamvault.password('<key>', site='benjamin-borbe'),   # SCREEGO_SECRET
    'users_file': teamvault.file('<key>', site='benjamin-borbe'),   # "<name>:<bcrypt>" lines
},
```

## Secrets

`SCREEGO_SECRET` and the users file (bcrypt login hashes) come from TeamVault via
`bwtv` — never inlined. Set them in the node metadata.

## Files rendered

- `/data/screego/environment` — `SCREEGO_*` env (mako, from metadata)
- `/data/screego/users` — `<name>:<bcrypt>` (from TeamVault)
- `/lib/systemd/system/screego.service` — docker-run unit (host net, `--env-file`)

## Ports (opened via the iptables reactor)

- `3478/tcp`, `5050/tcp` (web), `50000:50100/udp` (TURN relay)

## Enabled on

- `hz.hetzner-1`
