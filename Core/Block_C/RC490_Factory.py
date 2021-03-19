from Core.IFactory import IFactory
from Regs.Block_C import RC490


class RC490Factory(IFactory):

    def create_block_object(self, line):
        self.rc490 = _rc490 = RC490()
        _rc490.reg_list = line
        return _rc490
