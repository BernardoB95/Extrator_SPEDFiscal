from Core.IFactory import IFactory
from Regs.Block_C import RC191


class RC191Factory(IFactory):

    def create_block_object(self, line):
        self.rc191 = _rc191 = RC191()
        _rc191.reg_list = line
        return _rc191
