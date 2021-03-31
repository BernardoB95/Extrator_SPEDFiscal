from Core.IFactory import IFactory
from Regs.Block_K import RK235


class RK235Factory(IFactory):

    def create_block_object(self, line):
        self.rk235 = _rk235 = RK235()
        _rk235.reg_list = line
        return _rk235
