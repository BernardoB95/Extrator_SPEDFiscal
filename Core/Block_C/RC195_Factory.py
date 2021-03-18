from Core.IFactory import IFactory
from Regs.Block_C import RC195


class RC195Factory(IFactory):

    def create_block_object(self, line):
        self.rc195 = _rc195 = RC195()
        _rc195.reg_list = line
        return _rc195
