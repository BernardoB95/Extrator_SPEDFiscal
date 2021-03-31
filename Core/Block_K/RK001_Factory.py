from Core.IFactory import IFactory
from Regs.Block_K import RK001


class RK001Factory(IFactory):

    def create_block_object(self, line):
        self.rk001 = _rk001 = RK001()
        _rk001.reg_list = line
        return _rk001
