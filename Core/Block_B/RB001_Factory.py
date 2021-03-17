from Core.IFactory import IFactory
from Regs.Block_B import RB001


class RB001Factory(IFactory):

    def create_block_object(self, line):
        self.rb001 = _rb001 = RB001()
        _rb001.reg_list = line
        return  _rb001
