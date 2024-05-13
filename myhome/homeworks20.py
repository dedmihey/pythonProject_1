class Building:
    total = 0

    def __init__(self):
        Building.total += 1


quantity_object = []
for i in range(40):
    new_object = Building()
    quantity_object.append(new_object)

print(len(quantity_object))

