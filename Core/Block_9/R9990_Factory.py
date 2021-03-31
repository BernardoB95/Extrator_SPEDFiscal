from Core.IFactory import IFactory
from Regs.Block_9 import R9990


class R9990Factory(IFactory):

    def create_block_object(self, line):
        self.r9990 = _r9990 = R9990()
        _r9990.reg_list = line
        return _r9990
