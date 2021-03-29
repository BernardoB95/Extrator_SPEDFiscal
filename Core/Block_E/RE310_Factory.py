from Core.IFactory import IFactory
from Regs.Block_E import RE310


class RE310Factory(IFactory):

    def create_block_object(self, line):
        self.re310 = _re310 = RE310()
        _re310.reg_list = line
        return _re310
