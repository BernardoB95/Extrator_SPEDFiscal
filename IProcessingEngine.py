# Imports
from abc import ABC, abstractmethod
from Utils import load_factory, reg_logger, reg_size_logger, no_regs_identified_logger, Reader, Binder
from Regs import NullReg
from collections import defaultdict
from pandas import DataFrame, ExcelWriter
import os


class IProcessingEngine(ABC):

    def __init__(self, args):
        self._file_id = 0
        self.output_dir = args.output_dir
        self.choices = args.regs
        self.verbosity = args.verbose
        self.input_dir = args.input_dir

    @abstractmethod
    def main(self):
        """
        This is the real main function embedded in an engine that will orchestrate the app.
        """

        file_reader = Reader(self.input_dir)
        file_generator = file_reader.ReadFilesGenerator()

        if self.verbosity:
            message = 'Reading all .txt files from directory {}'.format(self.input_dir)
            self.print_message(message)

        self._file_id = 0
        for name, file in file_generator:

            if self.verbosity:
                message = "Extracting values from file: {0}".format(name)
                self.print_message(message)

            self._file_id += 1
            BINDING_PRINT_ONCE = True
            sped_dict = defaultdict(list)
            reg_binder = Binder()

            for index, line in enumerate(file):

                reg = line[1:5]

                reg_factory = load_factory(reg)

                reg_obj = reg_factory.create_block_object(line)

                reg_obj.id = index

                if self.verbosity and BINDING_PRINT_ONCE:
                    message = "Applying binding rule to the REGs"
                    self.print_message(message)
                    BINDING_PRINT_ONCE = False

                reg_binder.bind_id(reg_obj)

                if not isinstance(reg_obj, NullReg):
                    name_key = reg_obj.__class__.__name__
                    sped_dict[name_key].append(reg_obj)

                else:
                    reg_obj.reg = reg
                    reg_logger(reg, name)

                    if self.verbosity:
                        message = "A REG read in the file was not recognized as a valid one. Please, check out the log"
                        self.print_message(message)

            irregular_values = list()

            if self.verbosity:
                message = "Grouping information by REGs..."
                self.print_message(message)

            for k, v in sped_dict.items():

                header_ids = ['FILE_ID', 'ID', 'ID_SUPER']
                header = v[0].header
                header = header_ids + header

                reg_lst = []
                for obj in v:
                    reg_lst_ids = [self._file_id, obj.id, obj.id_super]
                    reg_line = reg_lst_ids + obj.reg_list
                    reg_lst.append(reg_line)

                reg = reg_lst[0][3]

                try:
                    if len(header) != len(reg_lst[0]):
                        raise Exception("Tamanho de arrays diferente no registro {}".format(reg))

                    # Delete non-selected REGs without going to log
                    if not any('R' + r == k for r in self.choices):
                        irregular_values.append(k)

                    reg_df = DataFrame(reg_lst, columns=header)
                    sped_dict[k] = reg_df

                except Exception:
                    reg_size_logger(reg, name, len(header), len(reg_lst[0]))
                    irregular_values.append(k)

                    if self.verbosity:
                        message = "A difference in REG size was found. Please, check out the log."
                        self.print_message(message)

                    continue

            # Delete irregular key, val
            for irreg_key in irregular_values:
                del sped_dict[irreg_key]

            # Export
            excel_name = name.split('\\')[-1]
            excel_output_name = excel_name.replace('.txt', '.xlsx')
            output_directory = os.path.join(self.output_dir, excel_output_name)

            try:

                with ExcelWriter(output_directory) as writer:
                    for k, v in sped_dict.items():
                        v.to_excel(writer, sheet_name=k, index=False, encoding='mbcs', engine='xlsxwriter')

            except IndexError:
                # If empty dictionary due to irregularities, then Index Error will be caught
                no_regs_identified_logger(name)

                if self.verbosity:
                    message = "No Regs identified in one of the files, please check the log."
                    self.print_message(message)

                continue

            if self.verbosity:
                message = "File {0} exported into directory: {1}".format(excel_output_name, self.output_dir)
                self.print_message(message)

    @abstractmethod
    def print_message(self, message):
        print(message)
