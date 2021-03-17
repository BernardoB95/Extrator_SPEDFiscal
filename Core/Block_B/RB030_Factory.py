from Core.IFactory import IFactory
from Regs.Block_B import RB030

class RB030Factory(IFactory):

    def create_block_object(self, line):
        self.rb030 = _rb030 = RB030()
        _rb030.reg_list = line
        return _rb030
