from Core.IFactory import IFactory
from Regs.Block_B import RB350


class RB350Factory(IFactory):

    def create_block_object(self, line):
        self.rb350 = _rb350 = RB350()
        _rb350.reg_list = line
        return _rb350
