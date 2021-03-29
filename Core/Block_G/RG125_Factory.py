from Core.IFactory import IFactory
from Regs.Block_G import RG125


class RG125Factory(IFactory):

    def create_block_object(self, line):
        self.rg125 = _rg125 = RG125()
        _rg125.reg_list = line
        return _rg125
