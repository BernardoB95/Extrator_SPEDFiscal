# Imports
from Utils import load_factory, reg_logger, reg_size_logger
from Regs import NullReg
from collections import defaultdict
from pandas import DataFrame, Series


class ProcessingEngine:

    def __init__(self, files):
        self._files = files
        self._file_id = 0

    def main(self):
        """
        This is the real main function embedded in an engine that will orchestrate the app.
        """

        self._file_id = 0
        for name, file in self._files.items():

            self._file_id += 1
            sped_dict = defaultdict(list)

            for line in file:

                reg = line[1:5]

                reg_factory = load_factory(reg)

                reg_obj = reg_factory.create_block_object(line)

                if not isinstance(reg_obj, NullReg):
                    print(reg_obj.header)
                    print(reg_obj.reg_list)

                    name_key = reg_obj.__class__.__name__
                    sped_dict[name_key].append(reg_obj)

                else:
                    reg_obj.reg = reg
                    reg_logger(reg, name)

            # TODO overwrite list to pandas DF

            for k, v in sped_dict.items():

                header = v[0].header
                reg_lst = [obj.reg_list for obj in v]

                try:
                    reg = reg_lst[0][0]
                    if len(header) != len(reg_lst[0]):
                        raise Exception("Tamanho de arrays diferente no registro {}".format(reg_lst[0][0]))

                    reg_df = DataFrame(reg_lst)
                    print(header)
                    print(reg_df)

                except:
                    reg_size_logger(reg, name, len(header), len(reg_lst[0]))
                    sped_dict.pop(k)
                    continue
