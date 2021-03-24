from Core.IFactory import IFactory
from Regs.Block_D import RD697


class RD697Factory(IFactory):

    def create_block_object(self, line):
        self.rd697 = _rd697 = RD697()
        _rd697.reg_list = line
        return _rd697
