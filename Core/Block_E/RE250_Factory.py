from Core.IFactory import IFactory
from Regs.Block_E import RE250


class RE250Factory(IFactory):

    def create_block_object(self, line):
        self.re250 = _re250 = RE250()
        _re250.reg_list = line
        return _re250
