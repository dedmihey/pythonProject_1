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
        self.queue = queue.Queue()
        self.custom = custom

    def run(self):
        for cust in range(self.custom):
            self.queue.put(cust)  # Клиенты подходят до открытия. Всех в очередь.
            time.sleep(1)


class Customer(Thread):
    def __init__(self, queue, custom):
        super().__init__()
        self.queue = queue.Queue()
        self.custom = custom

    def run(self):
        n = 1
        for i in range(self.custom):
            time.sleep(1)
            self.queue.get()  # Первые трое быстро занимают 3 стола.
            t = tables.pop(0)  # Четвёртому надо ждать освобождения стола.
            if n <= 3:
                print(f'Клиент №{i + 1} занял {t}')
            else:
                tables.append(t)
                print(f'Клиент №{i + 1} в ожидании')  # Следующие трое опять быстро
                time.sleep(5)  # занимают 3 стола и т.д.
                print(f'Клиент №{n - i} поел')
                n = 0
            n += 1


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

t1 = Cafe(queue, 20)
t2 = Customer(queue, 20)

t1.start()
t2.start()

t1.join()
t2.join()
