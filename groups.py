from os import walk
from os.path import join

from bundlewrap.metadata import atomic

import bwtv as teamvault

for root, dirs, files in walk(join(repo_path, "groups")):
    for filename in files:
        if filename.endswith(".py"):
            node = join(root, filename)
            with open(node, 'r', encoding='utf-8') as f:
                exec(f.read())
