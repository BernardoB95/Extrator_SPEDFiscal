from Core.IFactory import IFactory
from Regs.Block_B import RB460


class RB460Factory(IFactory):

    def create_block_object(self, line):
        self.rb460 = _rb460 = RB460()
        _rb460.reg_list = line
        return _rb460
