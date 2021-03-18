from Core.IFactory import IFactory
from Regs.Block_C import RC111


class RC111Factory(IFactory):

    def create_block_object(self, line):
        self.rc111 = _rc111 = RC111()
        _rc111.reg_list = line
        return _rc111
