
class SignalContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_sygnal(self):
        return self._strategy.signal()