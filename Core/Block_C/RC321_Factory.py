from Core.IFactory import IFactory
from Regs.Block_C import RC321


class RC321Factory(IFactory):

    def create_block_object(self, line):
        self.rc321 = _rc321 = RC321()
        _rc321.reg_list = line
        return _rc321
