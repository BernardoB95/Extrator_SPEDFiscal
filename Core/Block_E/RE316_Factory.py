from Core.IFactory import IFactory
from Regs.Block_E import RE316


class RE316Factory(IFactory):

    def create_block_object(self, line):
        self.re316 = _re316 = RE316()
        _re316.reg_list = line
        return _re316
