from .IReg import IReg


class NullReg(IReg):

    @property
    def reg(self):
        return self._reg

    @reg.setter
    def reg(self, r):
        self._reg = r

    def tell(self):
        print('This is the Null class')

    def header(self):
        pass
