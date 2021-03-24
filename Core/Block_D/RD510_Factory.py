from Core.IFactory import IFactory
from Regs.Block_D import RD510


class RD510Factory(IFactory):

    def create_block_object(self, line):
        self.rd510 = _rd510 = RD510()
        _rd510.reg_list = line
        return _rd510
