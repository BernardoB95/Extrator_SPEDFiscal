from Core.IFactory import IFactory
from Regs.Block_E import RE240


class RE240Factory(IFactory):

    def create_block_object(self, line):
        self.re240 = _re240 = RE240()
        _re240.reg_list = line
        return _re240
