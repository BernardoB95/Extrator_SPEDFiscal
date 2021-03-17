from Core.IFactory import IFactory
from Regs.Block_B import RB420

class RB420Factory(IFactory):

    def create_block_object(self, line):
        self.rb420 = _rb420 = RB420()
        _rb420.reg_list = line
        return _rb420
