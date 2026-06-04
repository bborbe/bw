# openclaw bundle

Installs standard tools and dependencies for OpenClaw AI assistant instances.

## What it installs

### APT packages
- `fd-find` - Fast file finder
- `bat` - Cat with syntax highlighting
- `fzf` - Fuzzy finder
- `trash-cli` - Safe file deletion
- `ripgrep` - Fast grep (also in workspace bundle)
- `jq` - JSON processor
- `gh` - GitHub CLI (also in workspace bundle)
- `ffmpeg` - Media processing (for whisper, video-frames skills)

### Python (via uv)
- `git-ai-sync` - Zero-token git sync with AI conflict resolution
- `dependency-updater` - Go/Python dependency updater

## Usage

Enable in node metadata:

```python
'openclaw': {
    'enabled': True,
},
```

### Matrix integration

Provision `~/.openclaw/.env` (chmod 0600) with Matrix credentials sourced from
TeamVault. Required only on nodes whose OpenClaw instance connects to a Matrix
homeserver. Disabled by default — opt in per node.

```python
'openclaw': {
    'enabled': True,
    'matrix': {
        'enabled': True,
        'homeserver': 'https://matrix.benjamin-borbe.de',
        'user_id': teamvault.username('7qGn5L', site='benjamin-borbe'),
        'password': teamvault.password('7qGn5L', site='benjamin-borbe'),
    },
},
```

`homeserver` is a plain URL (bwtv has no `.url()` helper — only `.file()`,
`.username()`, `.password()`). The TeamVault secret holds MXID (username field)
+ password. Per-instance accounts use their own TeamVault secret. Example
`7qGn5L` = `@openclaw:matrix.benjamin-borbe.de`.
