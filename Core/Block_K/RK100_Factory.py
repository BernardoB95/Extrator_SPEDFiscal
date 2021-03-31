from Core.IFactory import IFactory
from Regs.Block_K import RK100


class RK100Factory(IFactory):

    def create_block_object(self, line):
        self.rk100 = _rk100 = RK100()
        _rk100.reg_list = line
        return _rk100
