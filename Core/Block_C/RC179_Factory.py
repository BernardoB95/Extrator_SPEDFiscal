from Core.IFactory import IFactory
from Regs.Block_C import RC179


class RC179Factory(IFactory):

    def create_block_object(self, line):
        self.rc179 = _rc179 = RC179()
        _rc179.reg_list = line
        return _rc179
