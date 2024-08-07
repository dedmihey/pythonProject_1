from multiprocessing import Process


class WarehouseManager():
    def __init__(self):
        self.data = {}

    def process_request(self, req):
        if req[0] not in self.data:
            self.data[req[0]] = 0
        if req[1] == 'receipt':
            self.data[req[0]] += req[2]
        else:
            if self.data[req[0]] >= req[2]:
                self.data[req[0]] -= req[2]
        # print(self.data)

    def run(self):
        for i in requests:
            pr_ = Process(target=self.process_request(i))
            pr_.start()
            pr_.join()
        print(self.data)


if __name__ == '__main__':
    requests = [('product1', 'receipt', 100),
                ('product2', 'receipt', 150),
                ('product1', 'shipment', 30),
                ('product3', 'receipt', 200),
                ('product2', 'shipment', 50)]
    manager = WarehouseManager()
    manager.run()
