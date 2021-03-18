from Core.IFactory import IFactory
from Regs.Block_C import RC101


class RC101Factory(IFactory):

    def create_block_object(self, line):
        self.rc101 = _rc101 = RC101()
        _rc101.reg_list = line
        return _rc101
