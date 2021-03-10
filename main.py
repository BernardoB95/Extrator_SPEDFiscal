# Imports
import Utils
import config
from engine import ProcessingEngine

# SPED Reader
file_reader = Utils.Reader(config.DATA_DIR)
files = file_reader.ReadFiles()

# Separador

engine = ProcessingEngine(files)
engine.main()



# Extrator

# Output
