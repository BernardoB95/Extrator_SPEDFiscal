from Core.IFactory import IFactory
from Regs.Block_C import RC410


class RC410Factory(IFactory):

    def create_block_object(self, line):
        self.rc410 = _rc410 = RC410()
        _rc410.reg_list = line
        return _rc410
