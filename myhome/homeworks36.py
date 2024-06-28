import threading
from threading import Lock

lock = Lock()


class BankAccount:
    def __init__(self, bal, amount):
        self.bal = bal
        self.amount = amount


account1 = BankAccount(1000, 100)
account2 = BankAccount(1000, 150)



def deposit_task():
    for _ in range(5):
        with lock:
            account1.bal += account1.amount
            print(f'Баланс {account1.bal}, внесено {account1.amount}')


def withdraw_task():
    for _ in range(5):
        with lock:
            account2.bal -= account2.amount
            print(f'Баланс {account2.bal}, снято {account2.amount}')


print('Начальный баланс ', account1.bal)


ba1 = threading.Thread(target=deposit_task)
ba2 = threading.Thread(target=withdraw_task)

ba1.start()
ba2.start()

ba1.join()
ba2.join()


