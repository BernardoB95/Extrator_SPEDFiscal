from Core.IFactory import IFactory
from Regs.Block_K import RK210


class RK210Factory(IFactory):

    def create_block_object(self, line):
        self.rk210 = _rk210 = RK210()
        _rk210.reg_list = line
        return _rk210
