from abc import ABC, abstractmethod


class EarningStrategy(ABC):
    @abstractmethod
    def calculate(self, creator):
        pass