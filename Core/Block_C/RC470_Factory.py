from Core.IFactory import IFactory
from Regs.Block_C import RC470


class RC470Factory(IFactory):

    def create_block_object(self, line):
        self.rc470 = _rc470 = RC470()
        _rc470.reg_list = line
        return _rc470
