from Core.IFactory import IFactory
from Regs.Block_E import RE116


class RE116Factory(IFactory):

    def create_block_object(self, line):
        self.re116 = _re116 = RE116()
        _re116.reg_list = line
        return _re116
