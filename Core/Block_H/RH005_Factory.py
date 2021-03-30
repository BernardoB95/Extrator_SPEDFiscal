from Core.IFactory import IFactory
from Regs.Block_H import RH005


class RH005Factory(IFactory):

    def create_block_object(self, line):
        self.rh005 = _rh005 = RH005()
        _rh005.reg_list = line
        return _rh005
