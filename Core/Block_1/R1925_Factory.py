from Core.IFactory import IFactory
from Regs.Block_1 import R1925


class R1925Factory(IFactory):

    def create_block_object(self, line):
        self.r1925 = _r1925 = R1925()
        _r1925.reg_list = line
        return _r1925
