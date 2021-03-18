from Core.IFactory import IFactory
from Regs.Block_C import RC197


class RC197Factory(IFactory):

    def create_block_object(self, line):
        self.rc197 = _rc197 = RC197()
        _rc197.reg_list = line
        return _rc197
