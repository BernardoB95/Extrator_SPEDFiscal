from Core.IFactory import IFactory
from Regs.Block_D import RD190


class RD190Factory(IFactory):

    def create_block_object(self, line):
        self.rd190 = _rd190 = RD190()
        _rd190.reg_list = line
        return _rd190
