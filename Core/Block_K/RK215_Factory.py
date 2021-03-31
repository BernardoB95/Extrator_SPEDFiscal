from Core.IFactory import IFactory
from Regs.Block_K import RK215


class RK215Factory(IFactory):

    def create_block_object(self, line):
        self.rk215 = _rk215 = RK215()
        _rk215.reg_list = line
        return _rk215
