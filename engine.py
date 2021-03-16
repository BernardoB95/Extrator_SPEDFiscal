# Imports
from Utils import load_factory, reg_logger, reg_size_logger
from Regs import NullReg
from collections import defaultdict
from pandas import DataFrame, ExcelWriter
from config import DATA_DIR
import os


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
                    name_key = reg_obj.__class__.__name__
                    sped_dict[name_key].append(reg_obj)

                else:
                    reg_obj.reg = reg
                    reg_logger(reg, name)

            irregular_values = list()

            for k, v in sped_dict.items():

                header = v[0].header
                reg_lst = [obj.reg_list for obj in v]
                reg = reg_lst[0][0]

                try:
                    if len(header) != len(reg_lst[0]):
                        raise Exception("Tamanho de arrays diferente no registro {}".format(reg))

                    reg_df = DataFrame(reg_lst, columns=header)
                    sped_dict[k] = reg_df

                except Exception:
                    reg_size_logger(reg, name, len(header), len(reg_lst[0]))
                    irregular_values.append(k)
                    continue

            # Delete irregular key, val
            for irreg_key in irregular_values:
                del sped_dict[irreg_key]

            # Export
            for k, v in sped_dict.items():
                excel_output_name = "To Do Later.xlsx"
                directory = os.path.join(DATA_DIR, excel_output_name)
                with ExcelWriter(directory, mode='a') as writer:
                    v.to_excel(writer, sheet_name=k)
