# ip

Deploys the `bborbe/ip` echo service — a small HTTP service that returns the
caller's public IP. Runs as a Docker container under a systemd unit, bound to
`127.0.0.1:${port}` and fronted by an nginx vhost (e.g. `ip.benjamin-borbe.de`).

Migrated from the legacy `world` tool (`configuration/service/ip.go`).

## Metadata

```python
'ip': {
    'enabled': True,
    'version': '1.1.0',   # bborbe/ip image tag
    'port': 8000,          # host port (127.0.0.1), proxied by nginx
},
```

## Notes

- Container listens on `8080` internally; systemd maps it to `127.0.0.1:${port}`.
- Public exposure is via the nginx `ip` vhost (SSL) — the container port is not
  opened in iptables.
- Enabled on: `hz.hetzner-1`.
