from Core.IFactory import IFactory
from Regs.Block_C import RC595


class RC595Factory(IFactory):

    def create_block_object(self, line):
        self.rc595 = _rc595 = RC595()
        _rc595.reg_list = line
        return _rc595
