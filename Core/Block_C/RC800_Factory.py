from Core.IFactory import IFactory
from Regs.Block_C import RC800


class RC800Factory(IFactory):

    def create_block_object(self, line):
        self.rc800 = _rc800 = RC800()
        _rc800.reg_list = line
        return _rc800
