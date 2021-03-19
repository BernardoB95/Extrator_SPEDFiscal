from Core.IFactory import IFactory
from Regs.Block_C import RC600


class RC600Factory(IFactory):

    def create_block_object(self, line):
        self.rc600 = _rc600 = RC600()
        _rc600.reg_list = line
        return _rc600
