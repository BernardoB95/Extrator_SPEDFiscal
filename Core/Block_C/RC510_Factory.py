from Core.IFactory import IFactory
from Regs.Block_C import RC510


class RC500Factory(IFactory):

    def create_block_object(self, line):
        self.rc510 = _rc510 = RC510()
        _rc510.reg_list = line
        return _rc510
