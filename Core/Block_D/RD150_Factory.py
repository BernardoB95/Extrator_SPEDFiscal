from Core.IFactory import IFactory
from Regs.Block_D import RD150


class RD150Factory(IFactory):

    def create_block_object(self, line):
        self.rd150 = _rd150 = RD150()
        _rd150.reg_list = line
        return _rd150
