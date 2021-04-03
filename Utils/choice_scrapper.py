from os import walk


def scrapper():
    _files = []
    _matches = ['cpython', '__', 'Reg']

    for (dirpath, dirnames, filenames) in walk(r"C:\MyDevProjects\Extrator SPED Fiscal\Regs"):

        for name in filenames:

            if not any(m in name for m in _matches):
                _files.append(name.replace('.py', ''))

    return _files
