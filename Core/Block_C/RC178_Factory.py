from Core.IFactory import IFactory
from Regs.Block_C import RC178


class RC178Factory(IFactory):

    def create_block_object(self, line):
        self.rc178 = _rc178 = RC178()
        _rc178.reg_list = line
        return _rc178
