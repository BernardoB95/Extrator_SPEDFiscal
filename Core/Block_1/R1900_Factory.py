from Core.IFactory import IFactory
from Regs.Block_1 import R1900


class R1900Factory(IFactory):

    def create_block_object(self, line):
        self.r1900 = _r1900 = R1900()
        _r1900.reg_list = line
        return _r1900
