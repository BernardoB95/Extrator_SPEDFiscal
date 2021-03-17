from Core.IFactory import IFactory
from Regs.Block_B import RB035


class RB035Factory(IFactory):

    def create_block_object(self, line):
        self.rb035 = _rb035 = RB035()
        _rb035.reg_list = line
        return _rb035
