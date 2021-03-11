from abc import ABC, abstractmethod


class IFactory(ABC):

    @abstractmethod
    def create_block_object(self):
        pass

    # TODO Add getter and setters of hierarchy levels