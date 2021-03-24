from Core.IFactory import IFactory
from Regs.Block_D import RD101


class RD101Factory(IFactory):

    def create_block_object(self, line):
        self.rd101 = _rd101 = RD101()
        _rd101.reg_list = line
        return _rd101
