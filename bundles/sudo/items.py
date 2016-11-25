files = {
    '/etc/sudoers.d/users': {
        'source': 'users',
        'content_type': 'mako',
        'mode': '0440',
        'owner': 'root',
        'group': 'root',
    },
}
