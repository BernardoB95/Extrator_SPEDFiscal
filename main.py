# Imports
import os
import Utils
from engine import ProcessingEngine
from Utils import scrapper


if __name__ == "__main__":

    parser = Utils.ArgsParser(scrapper())
    args = parser.args

    # SPED Reader
    if args.verbose:
        print('Reading all .txt files from directory {}'.format(args.input_dir))

    file_reader = Utils.Reader(args.input_dir)
    files = file_reader.ReadFiles()

    # Separador

    engine = ProcessingEngine(files, args)
    engine.main()

    if args.verbose:
        print('Extraction completed.')
        os.system("pause")

# TODO Create executable and tag first release GitHub
# TODO Create GUI
