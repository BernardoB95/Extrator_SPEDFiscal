from Core.IFactory import IFactory
from Regs.Block_C import RC591


class RC591Factory(IFactory):

    def create_block_object(self, line):
        self.rc591 = _rc591 = RC591()
        _rc591.reg_list = line
        return _rc591
