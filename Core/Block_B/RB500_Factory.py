from Core.IFactory import IFactory
from Regs.Block_B import RB500


class RB500Factory(IFactory):

    def create_block_object(self, line):
        self.rb500 = _rb500 = RB500()
        _rb500.reg_list = line
        return _rb500
