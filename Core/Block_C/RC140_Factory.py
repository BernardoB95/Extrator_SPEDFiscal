from Core.IFactory import IFactory
from Regs.Block_C import RC140


class RC140Factory(IFactory):

    def create_block_object(self, line):
        self.rc140 = _rc140 = RC140()
        _rc140.reg_list = line
        return _rc140
