from Core.IFactory import IFactory
from Regs.Block_C import RC180


class RC180Factory(IFactory):

    def create_block_object(self, line):
        self.rc180 = _rc180 = RC180()
        _rc180.reg_list = line
        return _rc180
