from Core.IFactory import IFactory
from Regs.Block_9 import R9001


class R9001Factory(IFactory):

    def create_block_object(self, line):
        self.r9001 = _r9001 = R9001()
        _r9001.reg_list = line
        return _r9001
