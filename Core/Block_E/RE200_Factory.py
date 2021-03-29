from Core.IFactory import IFactory
from Regs.Block_E import RE200


class RE200Factory(IFactory):

    def create_block_object(self, line):
        self.re200 = _re200 = RE200()
        _re200.reg_list = line
        return _re200
