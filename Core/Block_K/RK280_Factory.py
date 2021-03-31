from Core.IFactory import IFactory
from Regs.Block_K import RK280


class RK280Factory(IFactory):

    def create_block_object(self, line):
        self.rk280 = _rk280 = RK280()
        _rk280.reg_list = line
        return _rk280
