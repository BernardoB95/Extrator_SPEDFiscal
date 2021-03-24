from Core.IFactory import IFactory
from Regs.Block_D import RD110


class RD110Factory(IFactory):

    def create_block_object(self, line):
        self.rd110 = _rd110 = RD110()
        _rd110.reg_list = line
        return _rd110
