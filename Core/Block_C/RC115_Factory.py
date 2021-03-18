from Core.IFactory import IFactory
from Regs.Block_C import RC115


class RC115Factory(IFactory):

    def create_block_object(self, line):
        self.rc115 = _rc115 = RC115()
        _rc115.reg_list = line
        return _rc115
