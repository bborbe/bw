from os import walk
from os.path import join
from collections.abc import Sequence, Mapping
import tomlkit

from bundlewrap.metadata import atomic

import bwtv as teamvault

# convert magicstrings in toml nodes

converters = {
    'decrypt': lambda x: vault.decrypt(x),
    'decrypt_file': lambda x: vault.decrypt_file(x),
    'teamvault_file': lambda x: teamvault.file(x),
    'teamvault_username': lambda x: teamvault.username(x),
    'teamvault_password': lambda x: teamvault.password(x),
}


def demagify(data):
    if isinstance(data, str):
        for name, converter in converters.items():
            if data.startswith(f'!{name}:'):
                return converter(data[len(name) + 2:])
        else:
            return data
    elif isinstance(data, Sequence):
        return [demagify(element) for element in data]
    elif isinstance(data, Mapping):
        return {key: demagify(value) for key, value in data.items()}
    else:
        return data


for data in nodes.values():
    assert type(data['metadata']) is tomlkit.container.Container
    data['metadata'] = demagify(data['metadata'])

# get python and instance file nodes

for root, dirs, files in walk(join(repo_path, "nodes")):
    for filename in files:
        if filename.endswith(".py"):
            node = join(root, filename)
            with open(node, 'r', encoding='utf-8') as f:
                exec(f.read())
