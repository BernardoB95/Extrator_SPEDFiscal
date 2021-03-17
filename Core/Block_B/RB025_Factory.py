from Core.IFactory import IFactory
from Regs.Block_B import RB025


class RB025Factory(IFactory):

    def create_block_object(self, line):
        self.rb025 = _rb025 = RB025()
        _rb025.reg_list = line
        return _rb025
