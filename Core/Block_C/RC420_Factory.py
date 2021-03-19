from Core.IFactory import IFactory
from Regs.Block_C import RC420


class RC420Factory(IFactory):

    def create_block_object(self, line):
        self.rc420 = _rc420 = RC420()
        _rc420.reg_list = line
        return _rc420
