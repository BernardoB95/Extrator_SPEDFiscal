from Core.IFactory import IFactory
from Regs.Block_H import RH030


class RH030Factory(IFactory):

    def create_block_object(self, line):
        self.rh030 = _rh030 = RH030()
        _rh030.reg_list = line
        return _rh030
