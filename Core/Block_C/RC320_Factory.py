from Core.IFactory import IFactory
from Regs.Block_C import RC320


class RC320Factory(IFactory):

    def create_block_object(self, line):
        self.rc320 = _rc320 = RC320()
        _rc320.reg_list = line
        return _rc320
