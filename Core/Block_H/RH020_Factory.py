from Core.IFactory import IFactory
from Regs.Block_H import RH020


class RH020Factory(IFactory):

    def create_block_object(self, line):
        self.rh020 = _rh020 = RH020()
        _rh020.reg_list = line
        return _rh020
