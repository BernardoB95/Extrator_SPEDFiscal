from Core.IFactory import IFactory
from Regs.Block_0 import R0500


class R0500Factory(IFactory):

    def create_block_object(self, line):
        self.r0500 = _r0500 = R0500()
        _r0500.reg_list = line
        return _r0500
