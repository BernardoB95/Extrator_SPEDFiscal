from Core.IFactory import IFactory
from Regs.Block_E import RE111


class RE111Factory(IFactory):

    def create_block_object(self, line):
        self.re111 = _re111 = RE111()
        _re111.reg_list = line
        return _re111
