from Core.IFactory import IFactory
from Regs.Block_E import RE311


class RE311Factory(IFactory):

    def create_block_object(self, line):
        self.re311 = _re311 = RE311()
        _re311.reg_list = line
        return _re311
