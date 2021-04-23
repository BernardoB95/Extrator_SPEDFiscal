from ..IReg import IReg


class R0305(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_CCUS',
                        'FUNC',
                        'VIDA_UTIL']

        self._hierarchy = "3"
