from Core.IFactory import IFactory
from Regs.Block_K import RK275


class RK25Factory(IFactory):

    def create_block_object(self, line):
        self.rk275 = _rk275 = RK275()
        _rk275.reg_list = line
        return _rk275
