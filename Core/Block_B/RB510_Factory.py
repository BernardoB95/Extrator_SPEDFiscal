from Core.IFactory import IFactory
from Regs.Block_B import RB510


class RB510Factory(IFactory):

    def create_block_object(self, line):
        self.rb510 = _rb510 = RB510()
        _rb510.reg_list = line
        return _rb510
