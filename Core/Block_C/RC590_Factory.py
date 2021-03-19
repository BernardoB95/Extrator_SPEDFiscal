from Core.IFactory import IFactory
from Regs.Block_C import RC590


class RC590Factory(IFactory):

    def create_block_object(self, line):
        self.rc590 = _rc590 = RC590()
        _rc590.reg_list = line
        return _rc590
