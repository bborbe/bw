# Monit Bundle

Manages [Monit](https://mmonit.com/monit/) system monitoring daemon.

## Features

- Installs and configures monit
- Manages monitrc and check configurations
- Optional mailserver configuration for alerts
- Optional test alert for verifying email delivery

## Configuration

### Basic Setup

Enable monit on a node via `groups/meta/monit.py` (enabled globally by default) or node metadata:

```python
'monit': {
    'enabled': True,
}
```

### Mailserver Configuration

Configure email alerts (already set globally in `groups/meta/monit.py`):

```python
'monit': {
    'enabled': True,
    'mailserver': {
        'server': 'mail.example.com',
        'port': 587,
        'username': 'alert@example.com',
        'password': 'secret',
        'recipient': 'admin@example.com',
        'sender': 'monit@hostname.example.com',
    },
}
```

### Custom Checks

Add custom monitoring checks:

```python
'monit': {
    'enabled': True,
    'checks': {
        'custom-check': {
            'template': 'my-check.conf',
            'context': {
                'threshold': 80,
            },
        },
    },
}
```

Place template at `bundles/monit/files/my-check.conf`.

### Test Alert Flag

Enable temporary test alert to verify email delivery:

```python
'monit': {
    'enabled': True,
    'test_alert': True,  # Add this temporarily
}
```

**What it does:**
- Adds a dummy file check (`/tmp/nonexistent-monit-test-file-xyz`)
- File never exists, so monit immediately sends an alert
- Useful for testing mailserver configuration

**Usage:**
1. Add `'test_alert': True` to node metadata
2. Apply: `bw apply <node>`
3. Check email inbox for test alert
4. **Remove flag** after verification
5. Apply again to clean up test check

**Note:** This is a testing feature — remove the flag after verification to avoid constant alerts.

## Files

- `items.py` — Bundle configuration
- `metadata.py` — Metadata reactors (mailserver, test_alert, etc.)
- `files/monitrc` — Main monit configuration template
- `files/mailserver.conf` — Mailserver configuration template
- `files/test-alert.conf` — Test alert check template
- `files/filesystem.conf` — Filesystem check template
- `files/http_check.conf` — HTTP check template

## Related

- Global monit config: `groups/meta/monit.py`
- TeamVault credentials: See `groups/meta/monit.py` for email auth
