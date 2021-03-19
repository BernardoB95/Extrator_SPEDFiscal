from Core.IFactory import IFactory
from Regs.Block_C import RC390


class RC390Factory(IFactory):

    def create_block_object(self, line):
        self.rc390 = _rc390 = RC390()
        _rc390.reg_list = line
        return _rc390
