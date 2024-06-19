import threading
import time


def list_1():
    for i in range(1, 11):
        print(i)
        time.sleep(1)


def list_2():
    n = 'abcdefghij'
    for k in n:
        print(k)
        time.sleep(1)


t1 = threading.Thread(target=list_1)
t2 = threading.Thread(target=list_2)
t1.start()
time.sleep(0.1)
t2.start()
t1.join()
t2.join()



