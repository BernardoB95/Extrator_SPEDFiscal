from Core.IFactory import IFactory
from Regs.Block_G import RG110


class RG110Factory(IFactory):

    def create_block_object(self, line):
        self.rg110 = _rg110 = RG110()
        _rg110.reg_list = line
        return _rg110
