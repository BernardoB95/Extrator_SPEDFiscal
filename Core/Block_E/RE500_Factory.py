from Core.IFactory import IFactory
from Regs.Block_E import RE500


class RE500Factory(IFactory):

    def create_block_object(self, line):
        self.re500 = _re500 = RE500()
        _re500.reg_list = line
        return _re500
