from Core.IFactory import IFactory
from Regs.Block_C import RC176


class RC176Factory(IFactory):

    def create_block_object(self, line):
        self.rc176 = _rc176 = RC176()
        _rc176.reg_list = line
        return _rc176
