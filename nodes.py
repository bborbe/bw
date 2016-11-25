from os import walk
from os.path import join

nodes = {}

for root, dirs, files in walk('nodes'):
    for filename in files:
        if filename.endswith('.py'):
            node = join(root, filename)
            with open(node, 'r') as f:
                exec (f.read())
