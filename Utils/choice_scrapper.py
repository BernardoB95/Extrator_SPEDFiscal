from os import walk
import config as cf


def scrapper():
    _files = []
    _matches = ['cpython', '__', 'Reg']

    for (dirpath, dirnames, filenames) in walk(cf.REGS_DIR):

        for name in filenames:

            if not any(m in name for m in _matches):
                _files.append(name.replace('.py', '').replace('R', ''))

    return _files
