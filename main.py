# Imports
import Utils
import config
from engine import ProcessingEngine

args = Utils.ArgsParser()

# SPED Reader
file_reader = Utils.Reader(config.DATA_DIR)
files = file_reader.ReadFiles()

# Separador

engine = ProcessingEngine(files)
engine.main()


# TODO Argparse (select regs)
# TODO Complete README file (intention, how to use, args menu, architecture, release, collaborations and PRs)
# TODO Create executable and tag first release GitHub
# TODO Create GUI
