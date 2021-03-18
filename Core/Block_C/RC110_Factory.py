from Core.IFactory import IFactory
from Regs.Block_C import RC110


class RC110Factory(IFactory):

    def create_block_object(self, line):
        self.rc110 = _rc110 = RC110()
        _rc110.reg_list = line
        return _rc110
