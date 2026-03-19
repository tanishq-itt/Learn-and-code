class VehicleManager:
    def __init__(self):
        self._vehicles = []

    def add_vehicle(self, vehicle):
        self._vehicles.append(vehicle)
        print(f"{type(vehicle).__name__} added")

    def display_all(self):
        print("\n=== Vehicles ===")
        for vehicle in self._vehicles:
            vehicle.display_info()

    def total_value(self):
        return sum(vehicle.price for vehicle in self._vehicles)

    def start_all(self):
        for vehicle in self._vehicles:
            vehicle.start()