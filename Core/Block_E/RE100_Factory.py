from Core.IFactory import IFactory
from Regs.Block_E import RE100


class RE100Factory(IFactory):

    def create_block_object(self, line):
        self.re100 = _re100 = RE100()
        _re100.reg_list = line
        return _re100
