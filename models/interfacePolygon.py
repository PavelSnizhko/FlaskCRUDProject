import abc



class PolygonInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_n(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_a(self):
        raise NotImplementedError()


    @abc.abstractmethod
    def set_n(self, n: int):
        raise NotImplementedError()

    @abc.abstractmethod
    def set_a(self, a):
        raise NotImplementedError()



