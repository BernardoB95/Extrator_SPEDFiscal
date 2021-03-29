from Core.IFactory import IFactory
from Regs.Block_E import RE510


class RE510Factory(IFactory):

    def create_block_object(self, line):
        self.re510 = _re510 = RE510()
        _re510.reg_list = line
        return _re510
