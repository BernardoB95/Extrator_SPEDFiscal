from Core.IFactory import IFactory
from Regs.Block_K import RK255


class RK255Factory(IFactory):

    def create_block_object(self, line):
        self.rk255 = _rk255 = RK255()
        _rk255.reg_list = line
        return _rk255
