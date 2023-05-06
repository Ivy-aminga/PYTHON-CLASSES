# Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively.
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
class Car:
    num_wheels = 4
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year