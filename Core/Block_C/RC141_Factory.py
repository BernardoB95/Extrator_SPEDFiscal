from Core.IFactory import IFactory
from Regs.Block_C import RC141


class RC141Factory(IFactory):

    def create_block_object(self, line):
        self.rc141 = _rc141 = RC141()
        _rc141.reg_list = line
        return _rc141
