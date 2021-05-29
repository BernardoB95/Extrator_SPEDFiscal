# Imports
from IProcessingEngine import IProcessingEngine


class ProcessingEngine(IProcessingEngine):


    def main(self):
        """
        This is the real main function embedded in an engine that will orchestrate the app.
        Default function from the Interface (Abstract Class)
        """
        super().main()

    def print_message(self, message):
        """
        This function will print to the console all of the verbosity messages.
        Default function from the Interface (Abstract Class)
        :param message: Verbosity message
        :type message: str
        """
        super().print_message(message)