from Core.IFactory import IFactory
from Regs.Block_C import RC400


class RC400Factory(IFactory):

    def create_block_object(self, line):
        self.rc400 = _rc400 = RC400()
        _rc400.reg_list = line
        return _rc400
