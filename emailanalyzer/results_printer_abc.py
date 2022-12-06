from abc import ABCMeta, abstractmethod


class ResultsPrinterABC(metaclass=ABCMeta):
    """By inheritance, enforces implementation of results printing functionality."""

    @abstractmethod
    def print_results(self):
        """To be implemented individually for every children."""
