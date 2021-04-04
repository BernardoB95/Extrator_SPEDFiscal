# Imports
from Utils import load_factory, reg_logger, reg_size_logger
from Regs import NullReg
from collections import defaultdict
from pandas import DataFrame, ExcelWriter
import os


class ProcessingEngine:

    def __init__(self, files, args):
        self._files = files
        self._file_id = 0
        self.output_dir = args.output_dir
        self.choices = args.regs
        self.verbosity = args.verbose


    def main(self):
        """
        This is the real main function embedded in an engine that will orchestrate the app.
        """

        self._file_id = 0
        for name, file in self._files.items():

            if self.verbosity:
                print("Extracting values from file: {0}".format(name))

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

                    if self.verbosity:
                        print("A REG read in the file was not recognized as a valid one. Please, check out the log")

            irregular_values = list()

            if self.verbosity:
                print("Grouping information by REGs...")

            for k, v in sped_dict.items():

                header = v[0].header
                reg_lst = [obj.reg_list for obj in v]
                reg = reg_lst[0][0]

                try:
                    if len(header) != len(reg_lst[0]):
                        raise Exception("Tamanho de arrays diferente no registro {}".format(reg))

                    # Delete non-selected REGs without going to log
                    if not any('R'+r == k for r in self.choices):
                        irregular_values.append(k)

                    reg_df = DataFrame(reg_lst, columns=header)
                    sped_dict[k] = reg_df

                except Exception:
                    reg_size_logger(reg, name, len(header), len(reg_lst[0]))
                    irregular_values.append(k)

                    if self.verbosity:
                        print("A difference in REG size was found. Please, check out the log.")

                    continue

            # Delete irregular key, val
            for irreg_key in irregular_values:
                del sped_dict[irreg_key]

            # Export
            excel_name = name.split('\\')[-1]
            excel_output_name = excel_name.replace('.txt', '.xlsx')
            output_directory = os.path.join(self.output_dir, excel_output_name)

            with ExcelWriter(output_directory) as writer:
                for k, v in sped_dict.items():

                    v.to_excel(writer, sheet_name=k, index=False)

            if self.verbosity:
                print("File {0} exported into directory: {1}".format(excel_output_name, self.output_dir))