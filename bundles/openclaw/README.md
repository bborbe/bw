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
