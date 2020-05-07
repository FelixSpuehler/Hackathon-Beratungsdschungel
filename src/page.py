from abc import ABCMeta, abstractmethod


class Page(metaclass=ABCMeta):
    """ Class for the pages """

    @abstractmethod
    def create_block_page(self):
        raise NotImplementedError
