from Core.IFactory import IFactory
from Regs.Block_C import RC890


class RC890Factory(IFactory):

    def create_block_object(self, line):
        self.rc890 = _rc890 = RC890()
        _rc890.reg_list = line
        return _rc890
