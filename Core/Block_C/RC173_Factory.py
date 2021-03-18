from Core.IFactory import IFactory
from Regs.Block_C import RC173


class RC173Factory(IFactory):

    def create_block_object(self, line):
        self.rc173 = _rc173 = RC173()
        _rc173.reg_list = line
        return _rc173
