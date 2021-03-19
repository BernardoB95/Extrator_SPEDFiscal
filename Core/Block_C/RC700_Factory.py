from Core.IFactory import IFactory
from Regs.Block_C import RC700


class RC700Factory(IFactory):

    def create_block_object(self, line):
        self.rc700 = _rc700 = RC700()
        _rc700.reg_list = line
        return _rc700
