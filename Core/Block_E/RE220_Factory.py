from Core.IFactory import IFactory
from Regs.Block_E import RE220


class RE220Factory(IFactory):

    def create_block_object(self, line):
        self.re220 = _re220 = RE220()
        _re220.reg_list = line
        return _re220
