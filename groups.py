from glob import glob
from os.path import join

groups = {}

for group in glob(join("groups", "*.py")):
    with open(group, 'r') as f:
        exec (f.read())
