import logging
import os
from Utils.argparser import ArgsParser
from Utils.choice_scrapper import scrapper

parser = ArgsParser(scrapper())
args = parser.args

logging.basicConfig(filename= os.path.join(args.output_dir, 'extrator.log'),
                    level=logging.WARNING,
                    filemode='w',
                    format='%(asctime)s; %(message)s')


def reg_logger(reg, filename):
    logging.warning('{0}; Registro nao configurado na ferramenta; REG{1}'.format(filename, reg))


def reg_size_logger(reg, filename, num, num_error):
    logging.error('{0}; Numero divergente de campos: {1} recebidos, nao {2}; REG{3}'.format(filename,
                                                                                            num,
                                                                                            num_error,
                                                                                            reg))
