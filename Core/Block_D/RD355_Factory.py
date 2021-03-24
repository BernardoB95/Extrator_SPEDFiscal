from Core.IFactory import IFactory
from Regs.Block_D import RD355


class RD355Factory(IFactory):

    def create_block_object(self, line):
        self.rd355 = _rd355 = RD355()
        _rd355.reg_list = line
        return _rd355
