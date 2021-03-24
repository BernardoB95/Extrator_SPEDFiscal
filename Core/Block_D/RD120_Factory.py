from Core.IFactory import IFactory
from Regs.Block_D import RD120


class RD120Factory(IFactory):

    def create_block_object(self, line):
        self.rd120 = _rd120 = RD120()
        _rd120.reg_list = line
        return _rd120
