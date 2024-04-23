class House:

    def __init__(self):
        self.numberOfFloors = 10

    def schet(self):
        print('Текущий этаж равен: ')


my_house = House()

House.numberOfFloors = 0
while House.numberOfFloors < 10:
    House.numberOfFloors += 1
    my_house.schet()
    print(House.numberOfFloors)
