from Core.IFactory import IFactory
from Regs.Block_C import RC860


class RC860Factory(IFactory):

    def create_block_object(self, line):
        self.rc860 = _rc860 = RC860()
        _rc860.reg_list = line
        return _rc860
