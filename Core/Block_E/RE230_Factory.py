from Core.IFactory import IFactory
from Regs.Block_E import RE230


class RE230Factory(IFactory):

    def create_block_object(self, line):
        self.re230 = _re230 = RE230()
        _re230.reg_list = line
        return _re230
