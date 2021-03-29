from Core.IFactory import IFactory
from Regs.Block_E import RE115


class RE115Factory(IFactory):

    def create_block_object(self, line):
        self.re115 = _re115 = RE115()
        _re115.reg_list = line
        return _re115
