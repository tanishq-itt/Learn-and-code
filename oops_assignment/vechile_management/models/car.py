from models.fuel_vehicle import FuelVehicle


class Car(FuelVehicle):
    def display_info(self):
        print(f"Car: {self._year} {self._make} {self._model}, Price: ${self._price}")