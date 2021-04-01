from Core.IFactory import IFactory
from Regs.Block_1 import R1105


class R1105Factory(IFactory):

    def create_block_object(self, line):
        self.r1105 = _r1105 = R1105()
        _r1105.reg_list = line
        return _r1105
