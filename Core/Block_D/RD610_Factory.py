from Core.IFactory import IFactory
from Regs.Block_D import RD610


class RD610Factory(IFactory):

    def create_block_object(self, line):
        self.rd610 = _rd610 = RD610()
        _rd610.reg_list = line
        return _rd610
