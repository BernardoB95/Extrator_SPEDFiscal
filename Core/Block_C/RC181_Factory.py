from Core.IFactory import IFactory
from Regs.Block_C import RC181


class RC181Factory(IFactory):

    def create_block_object(self, line):
        self.rc181 = _rc181 = RC181()
        _rc181.reg_list = line
        return _rc181
