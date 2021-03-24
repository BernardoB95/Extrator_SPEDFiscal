from Core.IFactory import IFactory
from Regs.Block_D import RD696


class RD696Factory(IFactory):

    def create_block_object(self, line):
        self.rd696 = _rd696 = RD696()
        _rd696.reg_list = line
        return _rd696
