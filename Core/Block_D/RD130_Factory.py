from Core.IFactory import IFactory
from Regs.Block_D import RD130


class RD130Factory(IFactory):

    def create_block_object(self, line):
        self.rd130 = _rd130 = RD130()
        _rd130.reg_list = line
        return _rd130
