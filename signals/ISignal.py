import abc


class ISignal(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def sygnal(self):
        pass
