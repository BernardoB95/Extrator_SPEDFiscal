from Core.IFactory import IFactory
from Regs.Block_D import RD161


class RD161Factory(IFactory):

    def create_block_object(self, line):
        self.rd161 = _rd161 = RD161()
        _rd161.reg_list = line
        return _rd161
