from Core.IFactory import IFactory
from Regs.Block_C import RC405


class RC405Factory(IFactory):

    def create_block_object(self, line):
        self.rc405 = _rc405 = RC405()
        _rc405.reg_list = line
        return _rc405
