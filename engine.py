# Imports
from Utils.loader import load_factory


class ProcessingEngine:

    def __init__(self, files):
        self._files = files


    def main(self):

        for name, file in self._files.items():

            for line in file:

                block = line[1:5]

                # TODO Create Factory with builder to instanciate
                obj = load_factory(block)