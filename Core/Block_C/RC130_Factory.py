from Core.IFactory import IFactory
from Regs.Block_C import RC130


class RC130Factory(IFactory):

    def create_block_object(self, line):
        self.rc130 = _rc130 = RC130()
        _rc130.reg_list = line
        return _rc130
