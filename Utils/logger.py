import logging

logging.basicConfig(filename='extrator.log',
                    level=logging.WARNING,
                    filemode='w',
                    format='%(asctime)s; %(message)s')


def reg_logger(reg):
    logging.warning('Registro nao configurado na ferramenta; REG{}'.format(reg))
