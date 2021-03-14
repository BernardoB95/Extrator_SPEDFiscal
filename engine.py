# Imports
from Utils import load_factory, reg_logger
from Regs import NullReg
from collections import defaultdict
from pandas import DataFrame, Series


class ProcessingEngine:

    def __init__(self, files):
        self._files = files
        self._file_id = 0

    def main(self):

        self._file_id = 0
        for name, file in self._files.items():

            self._file_id += 1
            sped_dict = defaultdict(list)

            for line in file:

                reg = line[1:5]

                # TODO Create Factory with builder to instantiate
                reg_factory = load_factory(reg)

                reg_obj = reg_factory.create_block_object(line)

                if not isinstance(reg_obj, NullReg):
                    print(reg_obj.header)

                    name_key = reg_obj.__class__.__name__
                    sped_dict[name_key].append(reg_obj)

                else:
                    reg_obj.reg = reg
                    reg_logger(reg)
