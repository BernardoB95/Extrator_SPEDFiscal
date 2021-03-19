from Core.IFactory import IFactory
from Regs.Block_C import RC880


class RC880Factory(IFactory):

    def create_block_object(self, line):
        self.rc880 = _rc880 = RC880()
        _rc880.reg_list = line
        return _rc880
