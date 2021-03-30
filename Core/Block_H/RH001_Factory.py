from Core.IFactory import IFactory
from Regs.Block_H import RH001


class RH001Factory(IFactory):

    def create_block_object(self, line):
        self.rh001 = _rh001 = RH001()
        _rh001.reg_list = line
        return _rh001
