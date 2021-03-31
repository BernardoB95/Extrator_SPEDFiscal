from Core.IFactory import IFactory
from Regs.Block_K import RK260


class RK260Factory(IFactory):

    def create_block_object(self, line):
        self.rk260 = _rk260 = RK260()
        _rk260.reg_list = line
        return _rk260
