from Core.IFactory import IFactory
from Regs.Block_C import RC310


class RC310Factory(IFactory):

    def create_block_object(self, line):
        self.rc310 = _rc310 = RC310()
        _rc310.reg_list = line
        return _rc310
