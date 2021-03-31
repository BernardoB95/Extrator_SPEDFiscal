from Core.IFactory import IFactory
from Regs.Block_9 import R9999


class R9999Factory(IFactory):

    def create_block_object(self, line):
        self.r9999 = _r9999 = R9999()
        _r9999.reg_list = line
        return _r9999
