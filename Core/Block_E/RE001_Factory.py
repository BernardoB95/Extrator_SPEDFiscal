from Core.IFactory import IFactory
from Regs.Block_E import RE001


class RE001Factory(IFactory):

    def create_block_object(self, line):
        self.re001 = _re001 = RE001()
        _re001.reg_list = line
        return _re001
