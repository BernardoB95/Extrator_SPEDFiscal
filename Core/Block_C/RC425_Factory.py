from Core.IFactory import IFactory
from Regs.Block_C import RC425


class RC425Factory(IFactory):

    def create_block_object(self, line):
        self.rc425 = _rc425 = RC425()
        _rc425.reg_list = line
        return _rc425
