from Core.IFactory import IFactory
from Regs.Block_G import RG140


class RG140Factory(IFactory):

    def create_block_object(self, line):
        self.rg140 = _rg140 = RG140()
        _rg140.reg_list = line
        return _rg140
