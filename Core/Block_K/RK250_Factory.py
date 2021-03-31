from Core.IFactory import IFactory
from Regs.Block_K import RK250


class RK250Factory(IFactory):

    def create_block_object(self, line):
        self.rk250 = _rk250 = RK250()
        _rk250.reg_list = line
        return _rk250
