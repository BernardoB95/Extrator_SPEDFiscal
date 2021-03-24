from Core.IFactory import IFactory
from Regs.Block_D import RD365


class RD365Factory(IFactory):

    def create_block_object(self, line):
        self.rd365 = _rd365 = RD365()
        _rd365.reg_list = line
        return _rd365
