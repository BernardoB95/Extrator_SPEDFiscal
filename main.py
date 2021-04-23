# Imports
import os
import Utils
from engine import ProcessingEngine
from Utils import scrapper
from datetime import datetime


if __name__ == "__main__":

    start = datetime.now()

    parser = Utils.ArgsParser(scrapper())
    args = parser.args

    engine = ProcessingEngine(args)
    engine.main()

    end = datetime.now()

    if args.verbose:
        exec_time = (end - start).seconds
        minutes = exec_time // 60
        seconds = exec_time - (minutes * 60)
        print('Extraction completed.')
        print('Process completed in {0}:{1:02d}'.format(minutes, seconds))
        os.system("pause")


# TODO Create GUI
