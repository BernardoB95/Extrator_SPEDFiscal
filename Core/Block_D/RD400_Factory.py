from Core.IFactory import IFactory
from Regs.Block_D import RD400


class RD400Factory(IFactory):

    def create_block_object(self, line):
        self.rd400 = _rd400 = RD400()
        _rd400.reg_list = line
        return _rd400
