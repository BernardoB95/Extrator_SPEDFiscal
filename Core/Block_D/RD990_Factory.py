from Core.IFactory import IFactory
from Regs.Block_D import RD990


class RD990Factory(IFactory):

    def create_block_object(self, line):
        self.rd990 = _rd990 = RD990()
        _rd990.reg_list = line
        return _rd990
