from Core.IFactory import IFactory
from Regs.Block_D import RD170


class RD170Factory(IFactory):

    def create_block_object(self, line):
        self.rd170 = _rd170 = RD170()
        _rd170.reg_list = line
        return _rd170
