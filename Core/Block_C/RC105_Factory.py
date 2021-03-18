from Core.IFactory import IFactory
from  Regs.Block_C import RC105


class RC105Factory(IFactory):

    def create_block_object(self, line):
        self.rc105 = _rc105 = RC105()
        _rc105.reg_list = line
        return _rc105
