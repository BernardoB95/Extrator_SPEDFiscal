from Core.IFactory import IFactory
from Regs.Block_B import RB440

class RB440Factory(IFactory):

    def create_block_object(self, line):
        self.rb440 = _rb440 = RB440()
        _rb440.reg_list = line
        return _rb440
