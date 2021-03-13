from abc import ABC, abstractmethod


class IReg(ABC):

    @abstractmethod
    def tell(self):
        pass

    @property
    def header(self):
        return self._header