from models.car import Car
from models.motorcycle import Motorcycle
from models.electric_car import ElectricCar
from services.vehicle_manager import VehicleManager


def main():
    print("=== Vehicle Management Demo ===\n")

    car = Car("Honda", "Accord", 2023, 28000, 100)
    motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2022, 7500, 80, False)
    electric_car = ElectricCar("Tesla", "Model 3", 2023, 42000, 100)

    print("Testing Vehicles:")
    car.start()
    car.display_info()
    car.stop()

    print()
    motorcycle.start()
    motorcycle.display_info()

    print()
    electric_car.start()
    electric_car.display_info()

    manager = VehicleManager()
    manager.add_vehicle(car)
    manager.add_vehicle(motorcycle)
    manager.add_vehicle(electric_car)

    manager.display_all()
    print(f"\nTotal Value: ${manager.total_value()}")

    print("\nStarting all vehicles:")
    manager.start_all()


if __name__ == "__main__":
    main()