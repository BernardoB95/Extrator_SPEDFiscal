from Core.IFactory import IFactory
from Regs.Block_0 import R0200


class R0200Factory(IFactory):

    def create_block_object(self, line):
        self.r0200 = _r0200 = R0200()
        _r0200.reg_list = line
        return _r0200
