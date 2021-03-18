from Core.IFactory import IFactory
from Regs.Block_C import RC116


class RC116Factory(IFactory):

    def create_block_object(self, line):
        self.rc116 = _rc116 = RC116()
        _rc116.reg_list = line
        return _rc116
