#1. Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
 # наслідувані від "Транспортний засіб". Наповніть класи атрибутами та методами на свій розсуд.
class Vehicle:
     speed = None
     range = None
     passenger = None

     def say_hello(self):
         msg = f'Hello, I\'m a Vehicle'
         return msg


class Car(Vehicle):

     def say_hello(self):
         msg = f'Hello, I\'m Car my speed {self.speed} kmph my range {self.range} km capacity {self.passenger} passenger'
         return msg


class Airplane(Vehicle):

     def say_hello(self):
         msg = f'Hello, I\'m Airplane my speed {self.speed} kmph my range {self.range} km capacity {self.passenger} passenger'
         return msg


class Ship(Vehicle):

     def say_hello(self):
         msg = f'Hello, I\'m Ship my speed {self.speed} kmph my range {self.range} km capacity {self.passenger} passenger'
         return msg


my_car = Car()
my_car.speed = 180
my_car.range = 800
my_car.passenger = 4
my_airplane = Airplane()
my_airplane.speed = 890
my_airplane.range = 3000
my_airplane.passenger = 160
my_ship = Ship()
my_ship.speed = 50
my_ship.range = 10000
my_ship.passenger = 3000
v = Vehicle()

print(v.say_hello())
print(my_car.say_hello())
print(my_airplane.say_hello())
print(my_ship.say_hello())

# 2.Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель". Виведіть на екран значення атрибутів обʼєктів
class A:
    attr = 'car'
    pass


class B:
    attr = 'airplane'
    pass


class C:
     attr = 'ship'
     pass


obj = A()
print( obj.attr)










