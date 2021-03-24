from Core.IFactory import IFactory
from Regs.Block_D import RD410


class RD410Factory(IFactory):

    def create_block_object(self, line):
        self.rd410 = _rd410 = RD410()
        _rd410.reg_list = line
        return _rd410
