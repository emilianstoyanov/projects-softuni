from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + 0.9):
            self.fuel_quantity -= distance * (self.fuel_consumption + 0.9)


    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + 1.6)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95



import unittest
class TestCar(unittest.TestCase):
    def setUp(self):
        pass

    def test_drive_not_enough_fuel(self):
        # Arrange
        car = Car(100, 3)

        #Act
        car.drive(40)

        self.assertEqual(car.fuel_quantity, 100)



