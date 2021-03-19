from Core.IFactory import IFactory
from Regs.Block_C import RC480


class RC480Factory(IFactory):

    def create_block_object(self, line):
        self.rc480 = _rc480 = RC480()
        _rc480.reg_list = line
        return _rc480
