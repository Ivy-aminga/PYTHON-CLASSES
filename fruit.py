# Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively.
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
class Fruit:
    is_healthy = True
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste