from Core.IFactory import IFactory
from Regs.Block_C import RC165


class RC165Factory(IFactory):

    def create_block_object(self, line):
        self.rc165 = _rc165 = RC165()
        _rc165.reg_list = line
        return _rc165
