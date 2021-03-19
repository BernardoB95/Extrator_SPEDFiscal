from Core.IFactory import IFactory
from Regs.Block_C import RC791


class RC791Factory(IFactory):

    def create_block_object(self, line):
        self.rc791 = _rc791 = RC791()
        _rc791.reg_list = line
        return _rc791
