from Core.IFactory import IFactory
from Regs.Block_E import RE990


class RE990Factory(IFactory):

    def create_block_object(self, line):
        self.re990 = _re990 = RE990()
        _re990.reg_list = line
        return _re990
