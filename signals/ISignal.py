import abc


class ISignal(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def signal(self):
        pass
