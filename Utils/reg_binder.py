# Imports
from Regs import NullReg
from itertools import count

class Binder:

    def __init__(self):
        self._memory_binding_dict = {}

    def bind_id(self, reg):

        try:
            if reg.hierarchy == "0":
                reg.id_super = None
                self._memory_binding_dict[reg.hierarchy] = reg

            elif isinstance(reg, NullReg):
                raise AttributeError

            else:
                hierarchy_super = str(int(reg.hierarchy) - 1)
                reg.id_super = self._memory_binding_dict[hierarchy_super].id
                self._memory_binding_dict[reg.hierarchy] = reg

        except AttributeError:
            pass
