from Core.IFactory import IFactory
from Regs.Block_D import RD690


class RD690Factory(IFactory):

    def create_block_object(self, line):
        self.rd690 = _rd690 = RD690()
        _rd690.reg_list = line
        return _rd690
