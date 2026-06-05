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

### Gateway lifecycle — Hermes-managed, NOT bw

Hermes owns its own gateway process via a **user-level** systemd unit
(`~/.config/systemd/user/hermes-gateway.service`, installed by the upstream
installer / `hermes gateway service install`). The Hermes CLI
(`hermes gateway restart/stop/run`) targets that unit.

bw does **not** install `/etc/systemd/system/hermes.service`. A system-level
unit fights upstream: Hermes detects it as "legacy" on every update, prints
a `migrate-legacy` warning, and the CLI tooling can't see / control it.
Earlier commits of this bundle did install one; current version actively
cleans it up (`file: delete: True`, `svc_systemd: running/enabled: False`).

What bw **does** do for lifecycle: enables **lingering** on the hermes user
so its user-systemd unit survives logout and starts at boot without anyone
logging in (`loginctl enable-linger hermes`, idempotent). Without this, the
user-systemd unit only runs while the hermes user is logged in via SSH.

### Credentials → `bw-credentials.env`, not `~/.hermes/.env`

`~/.hermes/.env` is **owned by Hermes** — Hermes's interactive setup writes
config + runtime state there (room IDs, allowlists, encryption flags, …)
that bw can't possibly know upfront. bw managing that file would erase
Hermes's state on every apply.

Instead, bw provisions a **separate** file `/home/<user>/.hermes/bw-credentials.env`
(chmod 0600) that the systemd unit loads via `EnvironmentFile=`. The
gateway process inherits bw-injected credentials at start; Hermes's
own `.env` stays untouched. Credential rotation flows TeamVault → `bw
apply` → systemd restart, without touching Hermes state.

The file is built from whatever credential blocks are `enabled`:

- `hermes.matrix.enabled = True` → adds `MATRIX_HOMESERVER` / `MATRIX_USER` / `MATRIX_PASSWORD` (`MATRIX_USER`, not `MATRIX_USER_ID` — openclaw uses `_ID`; different agents, different conventions)
- `hermes.brave.enabled = True` → adds `BRAVE_SEARCH_API_KEY`
- `hermes.telegram.enabled = True` → adds `TELEGRAM_BOT_TOKEN` + `TELEGRAM_ALLOWED_USERS`. The allowlist is **required** by this bundle (set to `""` only if open access is genuinely intentional) — Telegram's public bot API means anyone can DM an unlocked bot.

If no credential blocks are enabled, the file is deleted.

## Usage

Minimal:

```python
'hermes': {
    'enabled': True,
},
```

With Matrix + Brave:

```python
'hermes': {
    'enabled': True,
    'matrix': {
        'enabled': True,
        'homeserver': 'https://matrix.benjamin-borbe.de',
        'user_id': teamvault.username('<key>', site='benjamin-borbe'),
        'password': teamvault.password('<key>', site='benjamin-borbe'),
    },
    'brave': {
        'enabled': True,
        'api_key': teamvault.password('<key>', site='benjamin-borbe'),
    },
},
```
