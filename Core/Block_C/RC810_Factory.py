from Core.IFactory import IFactory
from Regs.Block_C import RC810


class RC810Factory(IFactory):

    def create_block_object(self, line):
        self.rc810 = _rc810 = RC810()
        _rc810.reg_list = line
        return _rc810
