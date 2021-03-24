from Core.IFactory import IFactory
from Regs.Block_D import RD197


class RD197Factory(IFactory):

    def create_block_object(self, line):
        self.rd197 = _rd197 = RD197()
        _rd197.reg_list = line
        return _rd197
