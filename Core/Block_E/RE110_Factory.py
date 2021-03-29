from Core.IFactory import IFactory
from Regs.Block_E import RE110


class RE110Factory(IFactory):

    def create_block_object(self, line):
        self.re110 = _re110 = RE110()
        _re110.reg_list = line
        return _re110
