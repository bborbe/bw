from os import walk
from os.path import join

groups = {}

for root, dirs, files in walk('groups'):
    for filename in files:
        if filename.endswith('.py'):
            group = join(root, filename)
            with open(group, 'r') as f:
                exec (f.read())
