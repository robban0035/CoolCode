import abc
import numpy as np

class Calculator(metaclass=abc.ABCMeta):
    def __init__(self, option):
        self.option = option

    @abc.abstractmethod
    def get_value(self):