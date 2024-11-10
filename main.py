#task1
class Car:
    def __init__(self, distance_km, time_h):
        self._distance_km = distance_km
        self._time_h = time_h

    @property
    def distance_km(self):
        return self._distance_km

    @distance_km.setter
    def distance_km(self, value):
        if value < 0:
            raise ValueError("Відстань не може бути від'ємною")
        self._distance_km = value

    @property
    def time_h(self):
        return self._time_h

    @time_h.setter
    def time_h(self, value):
        if value < 0:
            raise ValueError("Час не може бути від'ємним")
        self._time_h = value

    @property
    def average_speed(self):
        return self._distance_km / self._time_h


car1 = Car(300, 3)
print(car1.average_speed)
#task2
class Order:
    def __init__(self, items):
        self._items = items
    @property
    def items(self):
        return self._items

    @property
    def total_cost(self):
        total = 0
        for name, quantity, price in self._items:
            total += quantity * price
        return total

order1 = Order([("Лампа", 10, 5)])
print(order1.total_cost)
#task3
class Square:
    def __init__(self, side):
        self._side = side
    @property
    def side(self):
        return self._side
    @side.setter
    def side(self, value):
        if value <= 0:
            raise ValueError("Side length must be a positive number")
        self._side = value
    @property
    def area(self):
        return self.side ** 2
square = Square(4)
print("Side length:", square.side)
print("Area:", square.area)
# task4
class Person:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be a positive number")
        self._weight = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive number")
        self._height = value
    @property
    def bmi(self):
        return self.weight / (self.height ** 2)
person = Person(58, 1.64)
print("Weight:", person.weight)
print("Height:", person.height)
print("BMI:", person.bmi)