from Core.IFactory import IFactory
from Regs.Block_D import RD140


class RD140Factory(IFactory):

    def create_block_object(self, line):
        self.rd140 = _rd140 = RD140()
        _rd140.reg_list = line
        return _rd140
