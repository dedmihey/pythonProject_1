class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('Этажность дома ', floors)


house_ = House()
house_.setNewNumberOfFloors(9)
