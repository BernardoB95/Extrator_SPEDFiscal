from Core.IFactory import IFactory
from Regs.Block_C import RC175


class RC175Factory(IFactory):

    def create_block_object(self, line):
        self.rc175 = _rc175= RC175()
        _rc175.reg_list = line
        return _rc175
