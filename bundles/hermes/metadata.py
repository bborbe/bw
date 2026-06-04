defaults = {
    'hermes': {
        'enabled': False,
        'user': 'hermes',
        'matrix': {
            'enabled': False,
            'homeserver': None,
            'user_id': None,
            'password': None,
        },
        'brave': {
            'enabled': False,
            'api_key': None,
        },
        'telegram': {
            'enabled': False,
            'bot_token': None,
            'allowed_users': None,  # comma-separated numeric Telegram user IDs (prefer over @usernames — IDs survive handle changes)
        },
    },
}


@metadata_reactor.provides(
    'users',
)
def add_user(metadata):
    hermes = metadata.get('hermes', {})
    if not hermes.get('enabled', False):
        return {}
    user = hermes.get('user', 'hermes')
    return {
        'users': {
            user: {
                'enabled': True,
            },
        },
    }


@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    if not metadata.get('hermes', {}).get('enabled', False):
        return {}

    pkgs_install = (
        # CLI tools
        'bat',
        'fd-find',
        'ffmpeg',
        'fzf',
        'gh',
        'jq',
        'pipx',
        'ripgrep',
        'trash-cli',
        # Playwright Chromium system libs (Ubuntu 24.04 / Noble).
        # Source: microsoft/playwright nativeDeps.ts ubuntu24.04-x64.chromium.
        # Avoids the manual `sudo npx playwright install-deps chromium` step.
        'libasound2t64',
        'libatk-bridge2.0-0t64',
        'libatk1.0-0t64',
        'libatspi2.0-0t64',
        'libcairo2',
        'libcups2t64',
        'libdbus-1-3',
        'libdrm2',
        'libgbm1',
        'libglib2.0-0t64',
        'libnspr4',
        'libnss3',
        'libpango-1.0-0',
        'libx11-6',
        'libxcb1',
        'libxcomposite1',
        'libxdamage1',
        'libxext6',
        'libxfixes3',
        'libxkbcommon0',
        'libxrandr2',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs_install:
        result['apt']['packages'][package_name] = {
            'installed': True
        }
    return result
