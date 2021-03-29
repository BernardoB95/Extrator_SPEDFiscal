from Core.IFactory import IFactory
from Regs.Block_E import RE520


class RE520Factory(IFactory):

    def create_block_object(self, line):
        self.re520 = _re520 = RE520()
        _re520.reg_list = line
        return _re520
