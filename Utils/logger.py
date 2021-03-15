import logging

logging.basicConfig(filename='extrator.log',
                    level=logging.WARNING,
                    filemode='w',
                    format='%(asctime)s; %(message)s')


def reg_logger(reg, filename):
    logging.warning('{0}; Registro nao configurado na ferramenta; REG{1}'.format(filename, reg))
