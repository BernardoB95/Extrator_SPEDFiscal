from Core.IFactory import IFactory
from Regs.Block_K import RK230


class RK230Factory(IFactory):

    def create_block_object(self, line):
        self.rk230 = _rk230 = RK230()
        _rk230.reg_list = line
        return _rk230
