# hermes bundle

Provisions a Hermes Agent ([NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)) instance: linux user, standard CLI tools, optional Matrix credentials. Mirrors the `openclaw` bundle.

The Hermes binary itself is **not** managed by bw — install manually as the
`hermes` user via the upstream installer:

```bash
sudo su - hermes
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

## What it installs

### Linux user

Auto-injected via `users` metadata reactor when `hermes.enabled = True`. UID/GID `11021` defined in `groups/meta/user.py`. No need to also list `users.hermes` in the node config.

### APT packages

- `bat`, `fd-find`, `ffmpeg`, `fzf`, `gh`, `jq`, `ripgrep`, `trash-cli`

### Matrix credentials (opt-in)

Provisions `~/.hermes/.env` (chmod 0600) with `MATRIX_HOMESERVER` / `MATRIX_USER_ID` / `MATRIX_PASSWORD` when `hermes.matrix.enabled = True`. Disabled by default — opt in per node.

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
