from Core.IFactory import IFactory
from Regs.Block_K import RK200


class RK200Factory(IFactory):

    def create_block_object(self, line):
        self.rk200 = _rk200 = RK200()
        _rk200.reg_list = line
        return _rk200
