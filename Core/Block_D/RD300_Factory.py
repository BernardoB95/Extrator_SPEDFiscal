from Core.IFactory import IFactory
from Regs.Block_D import RD300


class RD300Factory(IFactory):

    def create_block_object(self, line):
        self.rd300 = _rd300 = RD300()
        _rd300.reg_list = line
        return _rd300
