from Core.IFactory import IFactory
from Regs.Block_D import RD420


class RD420Factory(IFactory):

    def create_block_object(self, line):
        self.rd420 = _rd420 = RD420()
        _rd420.reg_list = line
        return _rd420
