from models.vehicle import Vehicle


class FuelVehicle(Vehicle):
    def __init__(self, make, model, year, price, fuel_level):
        super().__init__(make, model, year, price)
        self._fuel_level = fuel_level

    def refuel(self, amount):
        if amount > 0:
            self._fuel_level += amount
            print(f"Refueled. Fuel level: {self._fuel_level}%")

    def start(self):
        if self._fuel_level > 0:
            self._is_running = True
            print(f"{self._make} {self._model} started.")
        else:
            print("Cannot start - no fuel!")