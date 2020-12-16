# Написать программу Город.
# Создать три отдельных объекта: City, Street, House.
# У города должны быть улицы (City -> [Street]), у улиц должны быть дома Street -> [House].
# У города есть улицы и дома и возможности их добавлять и удалять.
#
#    Улицы могут вместить случайное количество домов от 5 до 20.
#    Дома могут иметь случайное количество населения от 1 до 100.
#    Должна быть возможность наполнить город одним методом.
#    У города должен быть метод который вернет количество населения.
# *доп. Написать метод который сможет напечатать таблицей:
# Улица Дом Население
#    1   1         5
#    1   2         10
#    1   3         25
#                  и т.д.


from random import randint


class House:
    def __init__(self, number):
        self.population = randint(1, 100)
        self.number = number


class Street:
    def __init__(self, number):
        self.number = number
        self.houses = []
        for i in range(1, randint(6, 20)):
            self.houses.append(House(i))


class City:
    def __init__(self, name):
        self.name = name
        self.streets = []
        self.populate()

    def populate(self):
        for i in range(1, randint(2, 5)):
            self.streets.append(Street(i))

    def print_city(self):
        for street in self.streets:
            print(f'Street#:{street.number}')
            for house in street.houses:
                print(f'Street #{street.number} - House #{house.number} - population {house.population}')


my_city = City('Городок')
my_city.print_city()




