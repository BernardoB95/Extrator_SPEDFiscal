from Core.IFactory import IFactory
from Regs.Block_K import RK301


class RK301Factory(IFactory):

    def create_block_object(self, line):
        self.rk301 = _rk301 = RK301()
        _rk301.reg_list = line
        return _rk301
