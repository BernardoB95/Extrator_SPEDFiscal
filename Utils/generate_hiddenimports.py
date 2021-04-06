import os
from itertools import cycle

dirs = []
modules = []
_matches = ['cpython', '__', 'IFactory']

for (dirpath, dirnames, filenames) in os.walk(r"C:\MyDevProjects\Extrator SPED Fiscal\Core"):

    for dir in dirnames:
        if '__' not in dir:
            dirs.append(dir)

    for file in filenames:
        if not any(m in file for m in _matches):
            modules.append(file.replace('.py', ''))


dir_iter = cycle(dirs)

for i, mod in enumerate(modules):

    if 'Null' in mod:
        print("Core.{}'', ".format(mod), end='')
    else:
        reg = mod[1]
        _dir = next((d for d in dir_iter if reg == d[-1]), None)
        print("'Core.{0}.{1}', ".format(_dir, mod), end='')

    if i % 3 == 0:
        print('')
