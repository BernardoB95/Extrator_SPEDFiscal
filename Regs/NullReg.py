from .IReg import IReg


class NullReg(IReg):

    def tell(self):
        print('This is the Null class')