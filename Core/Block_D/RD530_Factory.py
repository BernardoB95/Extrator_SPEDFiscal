from Core.IFactory import IFactory
from Regs.Block_D import RD530


class RD530Factory(IFactory):

    def create_block_object(self, line):
        self.rd530 = _rd530 = RD530()
        _rd530.reg_list = line
        return _rd530
