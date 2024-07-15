import queue
from threading import Thread
import time


class Table:
    def __init__(self, number):
        self.number = number
        # self.is_busy = is_busy


class Cafe(Thread):
    def __init__(self, queue, custom):
        super().__init__()
        self.queue = queue
        self.custom = custom

    def run(self):
        for cust in range(self.custom):
            self.queue.put(cust)  # Клиенты подходят до открытия. Всех в очередь.
            time.sleep(1)


class Customer(Thread):
    def __init__(self, queue, custom):
        super().__init__()
        self.queue = queue
        self.custom = custom

    def run(self):
        global t
        n = 1
        for i in range(self.custom):
            time.sleep(1)
            if n <= 3:
                self.queue.get()  # Первые трое быстро занимают 3 стола.
                t = tables.pop(0)  # Четвёртому надо ждать освобождения стола.
                print(f'Клиент №{i + 1} занял {t}')

            else:
                self.queue.get()
                print(f'Клиент №{i + 1} в ожидании')  # Следующие трое опять быстро
                time.sleep(5)  # занимают 3 стола и т.д.
                print(f'Клиент №{i + 2 - n} поел')
                print(f'Клиент №{i + 1} занял {t}')
                n = 0
            tables.append(t)
            n += 1


table1 = Table('стол №1')
table2 = Table('стол №2')
table3 = Table('стол №3')
tables = [table1.number, table2.number, table3.number]
print(tables)

queue = queue.Queue()

t1 = Cafe(queue, 20)
t2 = Customer(queue, 20)

t1.start()
t2.start()

t1.join()
t2.join()
