import abc

class BASE_Localizer(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.name = 'LOCALIZER'

    @abc.abstractmethod
    def load_pattern(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def training(self):
        raise NotImplementedError()
