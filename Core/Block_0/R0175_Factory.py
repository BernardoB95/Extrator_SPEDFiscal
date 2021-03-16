from Core.IFactory import IFactory
from Regs.Block_0 import R0175


class R0175Factory(IFactory):

    def create_block_object(self, line):
        self.r0175 = _r0175 = R0175()
        _r0175.reg_list = line
        return _r0175
