from Core.IFactory import IFactory
from Regs.Block_K import RK270


class RK270Factory(IFactory):

    def create_block_object(self, line):
        self.rk270 = _rk270 = RK270()
        _rk270.reg_list = line
        return _rk270
