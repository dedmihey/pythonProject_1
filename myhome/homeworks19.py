from operator import eq


class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors
                and self.buildingType == other.buildingType)


building_1 = Building(10, 'многоэтажка')
building_2 = Building(5, 'хрущёвка')
print(eq(building_1, building_2))