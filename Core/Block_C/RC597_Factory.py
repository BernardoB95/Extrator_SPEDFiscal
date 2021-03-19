from Core.IFactory import IFactory
from Regs.Block_C import RC597


class RC597Factory(IFactory):

    def create_block_object(self, line):
        self.rc597 = _rc597 = RC597()
        _rc597.reg_list = line
        return _rc597
