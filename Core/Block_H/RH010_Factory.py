from Core.IFactory import IFactory
from Regs.Block_H import RH010


class RH010Factory(IFactory):

    def create_block_object(self, line):
        self.rh010 = _rh010 = RH010()
        _rh010.reg_list = line
        return _rh010
