from Core.IFactory import IFactory
from Regs.Block_C import RC114


class RC114Factory(IFactory):

    def create_block_object(self, line):
        self.rc114 = _rc114 = RC114()
        _rc114.reg_list = line
        return _rc114
