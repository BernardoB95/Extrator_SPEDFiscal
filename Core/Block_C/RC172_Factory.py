from Core.IFactory import IFactory
from Regs.Block_C import RC172


class RC172Factory(IFactory):

    def create_block_object(self, line):
        self.rc172 = _rc172 = RC172()
        _rc172.reg_list = line
        return _rc172
