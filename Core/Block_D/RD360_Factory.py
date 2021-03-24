from Core.IFactory import IFactory
from Regs.Block_D import RD360


class RD360Factory(IFactory):

    def create_block_object(self, line):
        self.rd360 = _rd360 =RD360()
        _rd360.reg_list = line
        return _rd360
