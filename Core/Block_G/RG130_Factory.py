from Core.IFactory import IFactory
from Regs.Block_G import RG130


class RG130Factory(IFactory):

    def create_block_object(self, line):
        self.rg130 = _rg130 = RG130()
        _rg130.reg_list = line
        return _rg130
