from Core.IFactory import IFactory
from Regs.Block_E import RE530


class RE530Factory(IFactory):

    def create_block_object(self, line):
        self.re530 = _re530 = RE530()
        _re530.reg_list = line
        return _re530
