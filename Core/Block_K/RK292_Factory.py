from Core.IFactory import IFactory
from Regs.Block_K import RK292


class RK292Factory(IFactory):

    def create_block_object(self, line):
        self.rk292 = _rk292 = RK292()
        _rk292.reg_list = line
        return _rk292
