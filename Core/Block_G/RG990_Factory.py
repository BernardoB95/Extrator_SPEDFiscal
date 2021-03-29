from Core.IFactory import IFactory
from Regs.Block_G import RG990


class RG990Factory(IFactory):

    def create_block_object(self, line):
        self.rg990 = _rg990 = RG990()
        _rg990.reg_list = line
        return _rg990
