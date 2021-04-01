from config import DATA_DIR

import argparse


class ArgsParser:

    def __init__(self):
        self.parser = _parser = argparse.ArgumentParser(description="Argument parser for SPED Fiscal extractor.")
        _parser.add_argument('-i', '--input_dir',
                             type=str,
                             default=DATA_DIR,
                             metavar='',
                             help='Specify the directory where SPEDs are located. Default value is in '
                                  "'Extrator SPED Fiscal/data'.")
        _parser.add_argument('-o', '--output_dir',
                             type=str,
                             default=DATA_DIR,
                             metavar='',
                             help='Specify the directory where the excel files will be saved. Default value is in '
                                  "'Extrator SPED Fiscal/data'.")
        _parser.add_argument('-v', '--verbose',
                             action='store_true',
                             default=False,
                             help='Specify verbosity of the process. Default value is False.')
        _parser.add_argument('-r', '--regs',
                             metavar='',
                             help='Specify the Regs to be exported separated by commas, as in the following example: '
                                  '0001,0150,0200,C100,C190. Default value will consider all regs identified per file.')

        self.args = _parser.parse_args()
        return self.args
