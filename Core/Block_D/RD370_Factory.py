from Core.IFactory import IFactory
from Regs.Block_D import RD370


class RD370Factory(IFactory):

    def create_block_object(self, line):
        self.rd370 = _rd370 = RD370()
        _rd370.reg_list = line
        return _rd370
