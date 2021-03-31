from Core.IFactory import IFactory
from Regs.Block_K import RK300


class RK300Factory(IFactory):

    def create_block_object(self, line):
        self.rk300 = _rk300 = RK300()
        _rk300.reg_list = line
        return _rk300
