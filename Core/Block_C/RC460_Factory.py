from Core.IFactory import IFactory
from Regs.Block_C import RC460


class RC460Factory(IFactory):

    def create_block_object(self, line):
        self.rc460 = _rc460 = RC460()
        _rc460.reg_list = line
        return _rc460
