from Core.IFactory import IFactory
from Regs.Block_C import RC300


class RC300Factory(IFactory):

    def create_block_object(self, line):
        self.rc300 = _rc300 = RC300()
        _rc300.reg_list =  line
        return _rc300
