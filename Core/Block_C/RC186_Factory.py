from Core.IFactory import IFactory
from Regs.Block_C import RC186


class RC186Factory(IFactory):

    def create_block_object(self, line):
        self.rc186 = _rc186 = RC186()
        _rc186.reg_list = line
        return _rc186
