from Core.IFactory import IFactory
from Regs.Block_D import RD350


class RD350Factory(IFactory):

    def create_block_object(self, line):
        self.rd350 = _rd350 = RD350()
        _rd350.reg_list = line
        return _rd350
