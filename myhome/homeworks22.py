class Car:
    price = 1000000
    power = 110
    def horse_powers(self):
        print('Мощность ', self.power)

class Nissan(Car):
    def price_power(self):
        print('Цена авто ', 1500000)
        print('Мощность ', 150)
class Kia(Car):
    def price_power(self):
        print('Цена авто ', 1200000)
        print('Мощность ', 120)

print('Если бы у меня был Nissan')
my_car = Nissan()
my_car.price_power()

print('а у жены Kia')
my_car = Kia()
my_car.price_power()



