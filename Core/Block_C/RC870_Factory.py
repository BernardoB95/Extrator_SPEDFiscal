from Core.IFactory import IFactory
from Regs.Block_C import RC870


class RC870Factory(IFactory):

    def create_block_object(self, line):
        self.rc870 = _rc870 = RC870()
        _rc870.reg_list = line
        return _rc870
