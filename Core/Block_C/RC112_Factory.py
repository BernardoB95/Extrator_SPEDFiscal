from Core.IFactory import IFactory
from Regs.Block_C import RC112


class RC112Factory(IFactory):

    def create_block_object(self, line):
        self.rc112 = _rc112 = RC112()
        _rc112.reg_list = line
        return _rc112
