from Core.IFactory import IFactory
from Regs.Block_E import RE531


class RE531Factory(IFactory):

    def create_block_object(self, line):
        self.re531 = _re531 = RE531()
        _re531.reg_list = line
        return _re531
