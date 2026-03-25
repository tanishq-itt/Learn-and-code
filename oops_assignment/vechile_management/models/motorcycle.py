from models.fuel_vehicle import FuelVehicle


class Motorcycle(FuelVehicle):
    def __init__(self, make, model, year, price, fuel_level, has_sidecar):
        super().__init__(make, model, year, price, fuel_level)
        self._has_sidecar = has_sidecar

    def display_info(self):
        print(f"Motorcycle: {self._year} {self._make} {self._model}, Sidecar: {self._has_sidecar}, Price: ${self._price}")