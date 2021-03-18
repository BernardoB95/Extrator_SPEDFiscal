from Core.IFactory import IFactory
from Regs.Block_C import RC113


class RC113Factory(IFactory):

    def create_block_object(self, line):
        self.rc113 = _rc113 = RC113()
        _rc113.reg_list = line
        return _rc113
