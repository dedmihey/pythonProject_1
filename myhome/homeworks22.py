class Car:
    price = 1000000

    def horse_powers(self):
        power = 110
        return(power)


class Nissan(Car):
    price = 1500000

    def price_power(self):
        power = 150
        print('Цена авто ', self.price)
        print('Мощность ', power)


class Kia(Car):
    price = 1200000

    def price_power(self):
        power = 120
        print('Цена авто ', self.price)
        print('Мощность ', power)


print('Если бы у меня был Nissan')
my_car = Nissan()
my_car.price_power()

print('а у жены Kia')
my_car = Kia()
my_car.price_power()
