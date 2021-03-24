from Core.IFactory import IFactory
from Regs.Block_D import RD160


class RD160Factory(IFactory):

    def create_block_object(self, line):
        self.rd160 = _rd160 = RD160()
        _rd160.reg_list = line
        return _rd160
