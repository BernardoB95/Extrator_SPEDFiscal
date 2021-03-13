from abc import ABC, abstractmethod


class IReg(ABC):

    @property
    def header(self):
        return self._header