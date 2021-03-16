from abc import ABC, abstractmethod


class IReg(ABC):

    @property
    def reg_list(self):
        return self._reg_line

    @reg_list.setter
    def reg_list(self, reg_line):
        raw_reg_line = reg_line.split('|')
        self._reg_line = raw_reg_line[1:-1]

    @property
    def header(self):
        return self._header