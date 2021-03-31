from Core.IFactory import IFactory
from Regs.Block_K import RK265


class RK265Factory(IFactory):

    def create_block_object(self, line):
        self.rk265 = _rk265 = RK265()
        _rk265.reg_list = line
        return _rk265
