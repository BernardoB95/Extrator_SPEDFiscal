# Imports
from Utils import load_factory
from Regs import NullReg


class ProcessingEngine:

    def __init__(self, files):
        self._files = files
        self._file_id = 0

    def main(self):

        self._file_id = 0
        for name, file in self._files.items():

            self._file_id += 1

            for line in file:

                reg = line[1:5]

                # TODO Create Factory with builder to instantiate
                reg_factory = load_factory(reg)

                reg_obj = reg_factory.create_block_object(line)

                if not isinstance(reg_obj, NullReg):
                    print(reg_obj.header)
                    print('wait')

                else:
                    reg_obj.reg = reg
                    print(reg_obj.reg)
