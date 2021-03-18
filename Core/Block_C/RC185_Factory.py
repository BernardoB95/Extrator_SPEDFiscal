from Core.IFactory import IFactory
from Regs.Block_C import RC185


class RC185Factory(IFactory):

    def create_block_object(self, line):
        self.rc185 = _rc185 = RC185()
        _rc185.reg_list = line
        return _rc185
