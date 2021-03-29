from Core.IFactory import IFactory
from Regs.Block_E import RE312


class RE312Factory(IFactory):

    def create_block_object(self, line):
        self.re312 = _re312 = RE312
        _re312.reg_list = line
        return _re312
