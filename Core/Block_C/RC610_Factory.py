from Core.IFactory import IFactory
from Regs.Block_C import RC610


class RC610Factory(IFactory):

    def create_block_object(self, line):
        self.rc610 = _rc610 = RC610()
        _rc610.reg_list = line
        return _rc610
