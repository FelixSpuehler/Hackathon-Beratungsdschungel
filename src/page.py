from abc import ABCMeta, abstractmethod


class Page(metaclass=ABCMeta):
    """ Class for the  """

    @abstractmethod
    def create_script_block(self):
        raise NotImplementedError
