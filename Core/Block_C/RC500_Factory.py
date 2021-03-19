from Core.IFactory import IFactory
from Regs.Block_C import RC500


class RC500Factory(IFactory):

    def create_block_object(self, line):
        self.rc500 = _rc500 = RC500()
        _rc500.reg_list = line
        return _rc500
