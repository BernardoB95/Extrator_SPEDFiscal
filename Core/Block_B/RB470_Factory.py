from Core.IFactory import IFactory
from Regs.Block_B import RB470


class RB470Factory(IFactory):

    def create_block_object(self, line):
        self.rb470 = _rb470 = RB470()
        _rb470.reg_list = line
        return _rb470
