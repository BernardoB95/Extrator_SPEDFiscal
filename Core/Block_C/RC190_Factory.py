from Core.IFactory import IFactory
from Regs.Block_C import RC190


class RC190Factory(IFactory):

    def create_block_object(self, line):
        self.rc190 = _rc190 = RC190()
        _rc190.reg_list = line
        return _rc190
