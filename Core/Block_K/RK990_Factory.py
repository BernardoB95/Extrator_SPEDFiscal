from Core.IFactory import IFactory
from Regs.Block_K import RK990


class RK990Factory(IFactory):

    def create_block_object(self, line):
        self.rk990 = _rk990 = RK990()
        _rk990.reg_list = line
        return _rk990
