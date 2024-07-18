def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


total = add(1, 4, 6, 5, 4, 33, 2, 1)
# print(total)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


calculation = calculate(2, add=3, multiply=5)
# print(calculation)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car()
print(my_car.make)
