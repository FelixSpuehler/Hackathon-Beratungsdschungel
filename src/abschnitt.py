from abc import ABCMeta, abstractmethod


class Abschnitt(metaclass=ABCMeta):
    """ Class for the  """

    @abstractmethod
    def createScriptBlock(self):
        raise NotImplementedError
