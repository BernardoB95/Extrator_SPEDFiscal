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

    @property
    def hierarchy(self):
        return  self._hierarchy

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, index):
        self._id = index

    @property
    def id_super(self):
        return self._id_super

    @id_super.setter
    def id_super(self, id_pai):
        self._id_super = id_pai
