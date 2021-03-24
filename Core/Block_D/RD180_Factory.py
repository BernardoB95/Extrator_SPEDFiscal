from Core.IFactory import IFactory
from Regs.Block_D import RD180


class RD180Factory(IFactory):

    def create_block_object(self, line):
        self.rd180 = _rd180 = RD180()
        _rd180.reg_list = line
        return _rd180
