from Core.IFactory import IFactory
from Regs.Block_D import RD100


class RD100Factory(IFactory):

    def create_block_object(self, line):
        self.rd100 = _rc100 = RD100()
        _rc100.reg_list = line
        return _rc100
