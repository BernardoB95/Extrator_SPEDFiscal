from ..IReg import IReg


class RB350(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_CTA',
                        'CTA_ISS',
                        'CTA_COSIF',
                        'QTD_OCOR',
                        'COD_SERV',
                        'VL_CONT',
                        'VL_BC_ISS',
                        'ALIQ_ISS',
                        'VL_ISS',
                        'COD_INF_OBS']
