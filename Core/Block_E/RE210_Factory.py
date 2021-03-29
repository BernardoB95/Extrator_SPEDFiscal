from Core.IFactory import IFactory
from Regs.Block_E import RE210


class RE210Factory(IFactory):

    def create_block_object(self, line):
        self.re210 = _re210 = RE210()
        _re210.reg_list = line
        return _re210
