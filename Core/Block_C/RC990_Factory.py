from Core.IFactory import IFactory
from Regs.Block_C import RC990


class RC990Factory(IFactory):

    def create_block_object(self, line):
        self.rc990 = _rc990 = RC990()
        _rc990.reg_list = line
        return _rc990
