from Core.IFactory import IFactory
from Regs.Block_1 import R1310


class R1310Factory(IFactory):

    def create_block_object(self, line):
        self.r1310 = _r1310 = R1310()
        _r1310.reg_list = line
        return _r1310
