from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, year, price):
        self._make = make
        self._model = model
        self._year = year
        self._price = None
        self.set_price(price)
        self._is_running = False

    @property
    def price(self):
        return self._price

    def set_price(self, price):
        if 0 <= price <= 1_000_000:
            self._price = price
        else:
            raise ValueError("Price must be between 0 and 1,000,000")

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        self._is_running = False
        print(f"{self._make} {self._model} stopped.")

    @abstractmethod
    def display_info(self):
        pass