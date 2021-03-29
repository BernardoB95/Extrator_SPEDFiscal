from Core.IFactory import IFactory
from Regs.Block_G import RG126


class RG126Factory(IFactory):

    def create_block_object(self, line):
        line.rg126 = _rg126 = RG126()
        _rg126.reg_list = line
        return _rg126
