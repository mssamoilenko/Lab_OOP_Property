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