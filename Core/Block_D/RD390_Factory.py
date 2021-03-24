from Core.IFactory import IFactory
from Regs.Block_D import  RD390


class RD390Factory(IFactory):

    def create_block_object(self, line):
        self.rd390 = _rd390 = RD390()
        _rd390.reg_list = line
        return _rd390
