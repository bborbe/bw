# bind

Deploys the Bind DNS server as a Docker container (host networking, binds `:53`
directly) under a systemd unit.

Migrated from the legacy `world` tool (`configuration/service/bind.go`).

## Image

`bborbe/bind:{git-tag}-{yyyymm}` (e.g. `1.4.1-202607`) — built from
[`github.com/bborbe/docker-bind`](https://github.com/bborbe/docker-bind) via its
Makefile (`make build upload`, house pattern). The legacy `world` tool
rebuilt + pushed a fresh monthly time-stamped tag on every apply; bw pins a
fixed tag instead — updates = build a new tag, bump `version` here.

## Metadata

```python
'bind': {
    'enabled': True,
    'version': '1.4.1-202607',  # bborbe/bind image tag
},
```

## Files rendered

- `/lib/systemd/system/bind.service` — docker-run unit (host net, `--memory=256m`,
  command `/usr/sbin/named -u bind -g -f -4`)

## Data

- `/data/bind` (host) → `/etc/bind` **and** `/var/lib/bind` (container) — zone
  files, journals, keys. Non-recursive mount-point management only; named owns
  the contents. Perms stay `root:root 0777` (live state world left; named writes
  journals as the container's `bind` user).

## Ports

- `53/tcp` + `53/udp` — host networking (no DNAT). The iptables ACCEPT rules
  live in the node's `iptables.rules.filter` metadata (`nodes/hz.hetzner-1.py`),
  predating this bundle — left there deliberately so this migration changes
  zero iptables state.

## Enabled on

- `hz.hetzner-1`
