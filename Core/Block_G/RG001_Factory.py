from Core.IFactory import IFactory
from Regs.Block_G import RG001


class RG001Factory(IFactory):

    def create_block_object(self, line):
        self.rg001 = _rg001 = RG001()
        _rg001.reg_list = line
        return _rg001
