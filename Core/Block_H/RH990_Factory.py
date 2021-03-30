from Core.IFactory import IFactory
from Regs.Block_H import RH990


class RH990Factory(IFactory):

    def create_block_object(self, line):
        self.rh990 = _rh990 = RH990()
        _rh990.reg_list = line
        return _rh990
