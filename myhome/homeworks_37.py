import threading
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 20:
            print(f"Посетитель номер {customer_number} прибыл.")
            customer_thread = Customer(customer_number, self)
            customer_thread.start()
            customer_number += 1
            time.sleep(1)

    def serve_customer(self, customer):
        table_found = False
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.number} сел за стол {table.number}. (начало обслуживания)")
                time.sleep(5)
                table.is_busy = False
                print(f"Посетитель номер {customer.number} покушал и ушёл.(конец обслуживания)")
                table_found = True
                break
        if not table_found:
            print(f"Посетитель номер {customer.number} ожидает свободный стол. ")
            self.queue.put(customer)
            self.queue.get()
            time.sleep(5)
            for table in self.tables:
                if not table.is_busy:
                    table.is_busy = True
                    print(f"Посетитель номер {customer.number} сел за стол {table.number}. (начало обслуживания)")
                    time.sleep(5)
                    table.is_busy = False
                    print(f"Посетитель номер {customer.number} покушал и ушёл.(конец обслуживания)")
                    table_found = True


# Класс для посетителей
class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.number = number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()
