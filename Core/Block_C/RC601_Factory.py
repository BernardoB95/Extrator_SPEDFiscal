from Core.IFactory import IFactory
from Regs.Block_C import RC601


class RC601Factory(IFactory):

    def create_block_object(self, line):
        self.rc601 = _rc601 = RC601()
        _rc601.reg_list = line
        return _rc601
