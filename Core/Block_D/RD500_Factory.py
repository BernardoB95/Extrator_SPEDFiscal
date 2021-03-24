from Core.IFactory import IFactory
from Regs.Block_D import RD500


class RD500Factory(IFactory):

    def create_block_object(self, line):
        self.rd500 = _rd500 = RD500()
        _rd500.reg_list = line
        return _rd500
