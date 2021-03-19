from Core.IFactory import IFactory
from Regs.Block_C import RC465


class RC465Factory(IFactory):

    def create_block_object(self, line):
        self.rc465 = _rc465 = RC465()
        _rc465.reg_list = line
        return _rc465
