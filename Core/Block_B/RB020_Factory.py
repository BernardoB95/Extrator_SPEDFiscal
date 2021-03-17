from Core.IFactory import IFactory
from Regs.Block_B import RB020


class RB020Factory(IFactory):

    def create_block_object(self, line):
        self.rb020 = _rb020 = RB020()
        _rb020.reg_list = line
        return _rb020
