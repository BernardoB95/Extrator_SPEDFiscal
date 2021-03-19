from Core.IFactory import IFactory
from Regs.Block_C import RC790


class RC790Factory(IFactory):

    def create_block_object(self, line):
        self.rc790 = _rc790 = RC790()
        _rc790.reg_list = line
        return _rc790
