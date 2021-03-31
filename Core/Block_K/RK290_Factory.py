from Core.IFactory import IFactory
from Regs.Block_K import RK290


class RK290Factory(IFactory):

    def create_block_object(self, line):
        self.rk290 = _rk290 = RK290()
        _rk290.reg_list = line
        return _rk290
