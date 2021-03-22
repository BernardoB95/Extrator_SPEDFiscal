from Core.IFactory import IFactory
from Regs.Block_D import RD001


class RD001Factory(IFactory):

    def create_block_object(self, line):
        self.rd001 = _rd001 = RD001()
        _rd001.reg_list = line
        return _rd001
