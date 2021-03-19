from Core.IFactory import IFactory
from Regs.Block_C import RC815


class RC815Factory(IFactory):

    def create_block_object(self, line):
        self.rc815 = _rc815 = RC815()
        _rc815.reg_list = line
        return _rc815
