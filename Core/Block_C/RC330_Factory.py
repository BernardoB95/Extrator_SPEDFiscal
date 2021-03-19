from Core.IFactory import IFactory
from Regs.Block_C import RC330


class RC330Factory(IFactory):

    def create_block_object(self, line):
        self.rc330 = _rc330 = RC330()
        _rc330.reg_list = line
        return _rc330
