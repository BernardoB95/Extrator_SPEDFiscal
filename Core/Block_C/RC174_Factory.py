from Core.IFactory import IFactory
from Regs.Block_C import RC174


class RC174Factory(IFactory):

    def create_block_object(self, line):
        self.rc174 = _rc174 = RC174()
        _rc174.reg_list = line
        return _rc174
