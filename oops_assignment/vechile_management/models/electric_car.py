from models.vehicle import Vehicle


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, price, battery_level):
        super().__init__(make, model, year, price)
        self._battery_level = battery_level

    def charge(self, amount):
        if amount > 0:
            self._battery_level += amount
            print(f"Charged. Battery level: {self._battery_level}%")

    def start(self):
        if self._battery_level > 0:
            self._is_running = True
            print(f"{self._make} {self._model} electric motor started.")
        else:
            print("Cannot start - battery dead!")

    def display_info(self):
        print(f"Electric Car: {self._year} {self._make} {self._model}, Price: ${self._price}")