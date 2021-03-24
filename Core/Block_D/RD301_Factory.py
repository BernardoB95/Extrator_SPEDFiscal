from Core.IFactory import IFactory
from Regs.Block_D import RD301


class RD301Factory(IFactory):

    def create_block_object(self, line):
        self.rd301 = _rd301 = RD301()
        _rd301.reg_list = line
        return _rd301
