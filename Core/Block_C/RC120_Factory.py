from Core.IFactory import IFactory
from Regs.Block_C import RC120


class RC120Factory(IFactory):

    def create_block_object(self, line):
        self.rc120 = _rc120 = RC120()
        _rc120.reg_list = line
        return _rc120
