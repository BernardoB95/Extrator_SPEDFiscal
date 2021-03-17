from Core.IFactory import IFactory
from Regs.Block_B import RB990


class RB990Factory(IFactory):

    def create_block_object(self, line):
        self.rb990 = _rb990 = RB990()
        _rb990.reg_list = line
        return _rb990
