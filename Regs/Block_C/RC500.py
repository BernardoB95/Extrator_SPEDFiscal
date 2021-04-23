from ..IReg import IReg


class RC500(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_OPER',
                        'IND_EMIT',
                        'COD_PART',
                        'COD_MOD',
                        'COD_SIT',
                        'SER',
                        'SUB',
                        'COD_CONS',
                        'NUM_DOC',
                        'DT_DOC',
                        'DT_E_S',
                        'VL_DOC',
                        'VL_DESC',
                        'VL_FORN',
                        'VL_SERV_NT',
                        'VL_TERC',
                        'VL_DA',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_BC_ICMS_ST',
                        'VL_ICMS_ST',
                        'COD_INF,',
                        'VL_PIS',
                        'VL_COFINS',
                        'TP_LIGACAO',
                        'COD_GRUPO_TENSAO',
                        'CHV_DOCe',
                        'FIN_DOCe',
                        'CHV_DOCe_REF',
                        'IND_DEST',
                        'COD_MUN_DEST',
                        'COD_CTA']

        self._hierarchy = "2"
