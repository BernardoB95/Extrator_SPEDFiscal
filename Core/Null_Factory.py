from .IFactory import IFactory
from Regs import NullReg


class Null_Factory(IFactory):

    def create_block_object(self):
        self.null = _null = NullReg()
        return _null
