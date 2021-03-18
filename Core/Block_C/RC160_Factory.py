from Core.IFactory import IFactory
from Regs.Block_C import RC160


class RC160Factory(IFactory):

    def create_block_object(self, line):
        self.rc160 = _rc160 = RC160()
        _rc160.reg_list = line
        return _rc160
