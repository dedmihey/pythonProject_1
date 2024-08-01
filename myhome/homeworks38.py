import time
from random import randint
from multiprocessing import Process



class WarehouseManager(Process):
    def __init__(self):
        self.data = {}
        super().__init__()

    def process_request(self):
        shipment = randint(0, 200)
        for i in products:
            # print(self.data)
            if self.data[i] >= shipment:
                self.data[i] = self.data.get(i) - shipment
                print(f'{i} отгрузка {shipment} в наличии {self.data[i]}')
            # time.sleep(6)

    def run(self):
        while True:
            for i in products:
                receipt = 0
                if i not in self.data:
                    self.data[i] = 0
                else:
                    receipt = randint(0, 200)
                    self.data[i] += receipt
                    print(f'{i} приход {receipt} в наличии {self.data[i]}')
                    time.sleep(5)
            # time.sleep(3)
            shipment_process = Process(target=self.process_request)
            shipment_process.start()


products = ['product1', 'product2', 'product3']

if __name__ == '__main__':
    receipt_process = WarehouseManager()
    receipt_process.start()
    receipt_process.join()
