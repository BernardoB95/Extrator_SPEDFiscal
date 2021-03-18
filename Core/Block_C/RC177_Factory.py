from Core.IFactory import IFactory
from Regs.Block_C import RC177


class RC177Factory(IFactory):

    def create_block_object(self, line):
        self.rc177 = _rc177 = RC177()
        _rc177.reg_list = line
        return _rc177
