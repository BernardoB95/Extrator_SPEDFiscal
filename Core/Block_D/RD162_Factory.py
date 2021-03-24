from Core.IFactory import IFactory
from Regs.Block_D import RD162


class RD162Factory(IFactory):

    def create_block_object(self, line):
        self.rd162 = _rd162 = RD162()
        _rd162.reg_list = line
        return _rd162
