from Core.IFactory import IFactory
from Regs.Block_C import RC100


class RC100Factory(IFactory):

    def create_block_object(self, line):
        self.rc100 = _rc100 = RC100()
        _rc100.reg_list = line
        return _rc100
