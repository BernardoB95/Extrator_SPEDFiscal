from Core.IFactory import IFactory
from Regs.Block_D import RD600


class RD600Factory(IFactory):

    def create_block_object(self, line):
        self.rd600 = _rd600 = RD600()
        _rd600.reg_list = line
        return _rd600
