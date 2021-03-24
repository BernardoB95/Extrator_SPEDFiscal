from Core.IFactory import IFactory
from Regs.Block_D import RD310


class RD310Factory(IFactory):

    def create_block_object(self, line):
        self.rd310 = _rd310 = RD310()
        _rd310.reg_list = line
        return _rd310
