from Core.IFactory import IFactory
from Regs.Block_E import RE112


class RE112Factory(IFactory):

    def create_block_object(self, line):
        self.re112 = _re112 = RE112()
        _re112.reg_list = line
        return _re112
