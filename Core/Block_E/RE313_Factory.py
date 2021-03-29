from Core.IFactory import IFactory
from Regs.Block_E import RE313


class RE313Factory(IFactory):

    def create_block_object(self, line):
        self.re313 = _re313 = RE313()
        _re313.reg_list = line
        return _re313
