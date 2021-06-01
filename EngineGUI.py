from IProcessingEngine import IProcessingEngine


class ProcessingEngine(IProcessingEngine):

    def __init__(self, args, signal):
        super().__init__(args)
        self.signal = signal

    def main(self):
        super().main()

    def print_message(self, message):
        self.signal.emit(message)