from Core.IFactory import IFactory
from Regs.Block_C import RC350


class RC350Factory(IFactory):

    def create_block_object(self, line):
        self.rc350 = _rc350 = RC350()
        _rc350.reg_list = line
        return _rc350
