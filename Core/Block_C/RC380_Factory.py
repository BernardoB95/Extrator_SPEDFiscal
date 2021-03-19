from Core.IFactory import IFactory
from Regs.Block_C import RC380


class RC380Factory(IFactory):

    def create_block_object(self, line):
        self.rc380 = _rc380 = RC380()
        _rc380.reg_list = line
        return _rc380
