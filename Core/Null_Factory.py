from .IFactory import IFactory


class Null_Factory(IFactory):

    def create_block_object(self):
        pass