# Imports
import Utils
import config
from engine import ProcessingEngine
from Utils import scrapper


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

# TODO Complete README file (intention, how to use, args menu, architecture, release, collaborations and PRs)
# TODO Create executable and tag first release GitHub
# TODO Create GUI
