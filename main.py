# Imports
import Utils
import config
from engine import ProcessingEngine
from Utils import scrapper


parser = Utils.ArgsParser(scrapper())
args = parser.args

# SPED Reader
file_reader = Utils.Reader(args.input_dir)
files = file_reader.ReadFiles()

# Separador

engine = ProcessingEngine(files, args)
engine.main()


# TODO Argparse (select regs)
# TODO Complete README file (intention, how to use, args menu, architecture, release, collaborations and PRs)
# TODO Create executable and tag first release GitHub
# TODO Create GUI
