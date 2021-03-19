from Core.IFactory import IFactory
from Regs.Block_C import RC690


class RC690Factory(IFactory):

    def create_block_object(self, line):
        self.rc690 = _rc690 = RC690()
        _rc690.reg_list = line
        return _rc690
