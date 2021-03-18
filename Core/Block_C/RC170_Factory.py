from Core.IFactory import IFactory
from Regs.Block_C import RC170


class RC170Factory(IFactory):

    def create_block_object(self, line):
        self.rc170 = _rc170 = RC170()
        _rc170.reg_list = line
        return _rc170
