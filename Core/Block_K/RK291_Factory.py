from Core.IFactory import IFactory
from Regs.Block_K import RK291


class RK291Factory(IFactory):

    def create_block_object(self, line):
        self.rk291 = _rk291 = RK291()
        _rk291.reg_list = line
        return _rk291
