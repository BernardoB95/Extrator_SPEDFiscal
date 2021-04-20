from abc import ABC, abstractmethod


class IFactory(ABC):

    @abstractmethod
    def create_block_object(self, line):
        pass

