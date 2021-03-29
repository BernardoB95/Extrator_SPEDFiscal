from Core.IFactory import IFactory
from Regs.Block_E import RE300


class RE300Factory(IFactory):

    def create_block_object(self, line):
        self.re300 = _re300 = RE300()
        _re300.reg_list = line
        return _re300
