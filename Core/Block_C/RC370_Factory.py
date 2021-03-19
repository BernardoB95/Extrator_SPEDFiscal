from Core.IFactory import IFactory
from Regs.Block_C import RC370


class RC370Factory(IFactory):

    def create_block_object(self, line):
        self.rc370 = _rc370 = RC370()
        _rc370.reg_list = line
        return _rc370
