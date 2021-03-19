from Core.IFactory import IFactory
from Regs.Block_C import RC850


class RC850Factory(IFactory):

    def create_block_object(self, line):
        self.rc850 = _rc850 = RC850()
        _rc850.reg_list = line
        return _rc850
