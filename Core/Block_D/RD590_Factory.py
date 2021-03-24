from Core.IFactory import IFactory
from Regs.Block_D import RD590


class RD590Factory(IFactory):

    def create_block_object(self, line):
        self.rd590 = _rd590 = RD590()
        _rd590.reg_list = line
        return _rd590
