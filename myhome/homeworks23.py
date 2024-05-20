class Vehicle:
    vehicle_type = "none"

    def __init__(self):
        pass

class Car:
    price = 1000000

    def horse_powers(self):
        power = 110
        return(power)

class Nissan(Car, Vehicle):
    vehicle_type = "Nissan"
    price = 1500000

    def horse_powers(self):
        self.power = 150
        print('Марка авто ', self.vehicle_type)
        print('Цена авто ', self.price)
        print('Мощность ', self.power)

my_car = Nissan()
my_car.horse_powers()



