from Core.IFactory import IFactory
from Regs.Block_C import RC001


class RC001Factory(IFactory):

    def create_block_object(self, line):
        self.rc001 = _rc001 = RC001()
        _rc001.reg_list = line
        return _rc001
