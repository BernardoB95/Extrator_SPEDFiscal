from Core.IFactory import IFactory
from Regs.Block_9 import R9900


class R9900Factory(IFactory):

    def create_block_object(self, line):
        self.r9900 = _r9900 = R9900()
        _r9900.reg_list = line
        return _r9900
