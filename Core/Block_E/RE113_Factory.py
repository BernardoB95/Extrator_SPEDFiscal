from Core.IFactory import IFactory
from Regs.Block_E import RE113


class RE113Factory(IFactory):

    def create_block_object(self, line):
        self.re113 = _re113 = RE113()
        _re113.reg_list = line
        return _re113
