"""
OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
"""
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

Ferrari = Vehicle(215, 10)

print(Ferrari.max_speed, Ferrari.mileage)

"""
OOP Exercise 2: Create a Vehicle class without any variables and methods
"""
class EmptyVehicle:
    def __init__(self):
        pass # Nothing happens

Empty = EmptyVehicle()
print(Empty)

"""
OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
"""
class NamedVehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(NamedVehicle):
    pass

MTA = Bus("BX36", 25, 10000)
print("MTA", MTA.name, MTA.max_speed, MTA.mileage)

"""
OOP Exercise 4: Class Inheritance
Given:
Create a Bus class that inherits from the Vehicle class.
Give the capacity argument of Bus.seating_capacity() a default value of 50.
"""

class VehicleWithCapacity:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = 50

    def seating_capacity(self, capacity=None):
        if capacity is None:
            capacity = self.capacity
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class BusWithCapacity(VehicleWithCapacity):
    pass

bus = BusWithCapacity("bus", 25, 200)
print(bus.seating_capacity())