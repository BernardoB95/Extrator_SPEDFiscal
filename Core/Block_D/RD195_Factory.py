from Core.IFactory import IFactory
from Regs.Block_D import RD195


class RD195Factory(IFactory):

    def create_block_object(self, line):
        self.rd195 = _rd195 = RD195()
        _rd195.reg_list = line
        return _rd195
