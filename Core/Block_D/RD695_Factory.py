from Core.IFactory import IFactory
from Regs.Block_D import RD695


class RD695Factory(IFactory):

    def create_block_object(self, line):
        self.rd695 = _rd695 = RD695()
        _rd695.reg_list = line
        return _rd695
