from Core.IFactory import IFactory
from Regs.Block_C import RC171


class RC171Factory(IFactory):

    def create_block_object(self, line):
        self.rc171 = _rc171 = RC171()
        _rc171.reg_list = line
        return _rc171
