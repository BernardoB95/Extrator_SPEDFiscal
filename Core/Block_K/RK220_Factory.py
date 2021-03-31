from Core.IFactory import IFactory
from Regs.Block_K import RK220

class RK220Factory(IFactory):

    def create_block_object(self, line):
        self.rk220 = _rk220 = RK220()
        _rk220.reg_list = line
        return _rk220
