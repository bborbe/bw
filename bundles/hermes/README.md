# hermes bundle

Provisions a Hermes Agent ([NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)) instance: linux user, standard CLI tools, optional Matrix credentials. Mirrors the `openclaw` bundle.

The Hermes binary itself is **not** managed by bw (no .deb/release tarball
upstream yet) — install manually as the `hermes` user via the upstream
installer (auto-detects pipx and installs into
`~/.local/share/pipx/venvs/hermes-agent/`, symlinking `~/.local/bin/hermes`):

```bash
sudo su - hermes
pipx ensurepath                   # pipx is installed by this bundle's apt deps
exec $SHELL                       # reload PATH
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes doctor
hermes --version
```

## What it installs

### Linux user

Auto-injected via `users` metadata reactor when `hermes.enabled = True`. UID/GID `11021` defined in `groups/meta/user.py`. No need to also list `users.hermes` in the node config.

### APT packages

- `bat`, `fd-find`, `ffmpeg`, `fzf`, `gh`, `jq`, `ripgrep`, `trash-cli`

### Systemd unit

`/etc/systemd/system/hermes.service` — runs `~/.local/bin/hermes gateway` as
the `hermes` user. Enabled + running when `hermes.enabled = True`. Restarts
on env-file changes. (Note: still requires the Hermes binary to be
installed first via the upstream curl|bash above — the service will
fail-loop until then.)

### Matrix credentials (opt-in)

Provisions `~/.hermes/.env` (chmod 0600) with `MATRIX_HOMESERVER` / `MATRIX_USER` / `MATRIX_PASSWORD` when `hermes.matrix.enabled = True`. Disabled by default — opt in per node. (`MATRIX_USER`, not `MATRIX_USER_ID` — the openclaw env var. Different agents, different conventions.)

## Usage

Minimal:

```python
'hermes': {
    'enabled': True,
},
```

With Matrix:

```python
'hermes': {
    'enabled': True,
    'matrix': {
        'enabled': True,
        'homeserver': 'https://matrix.benjamin-borbe.de',
        'user_id': teamvault.username('<key>', site='benjamin-borbe'),
        'password': teamvault.password('<key>', site='benjamin-borbe'),
    },
},
```
