from Core.IFactory import IFactory
from Regs.Block_K import RK302


class RK302Factory(IFactory):

    def create_block_object(self, line):
        self.rk302 = _rk302 = RK302()
        _rk302.reg_list = line
        return _rk302
