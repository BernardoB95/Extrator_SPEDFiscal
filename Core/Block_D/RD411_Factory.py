from Core.IFactory import IFactory
from Regs.Block_D import RD411


class RD411Factory(IFactory):

    def create_block_object(self, line):
        self.rd411 = _rd411 = RD411()
        _rd411.reg_list = line
        return _rd411
