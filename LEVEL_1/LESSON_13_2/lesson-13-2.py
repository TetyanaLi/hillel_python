#Написать программу кофейный магазин.

#Обьекты:
#   Product
#   - свойства: наименование, тип, цена
#   - print обьекта продукта должен возвращать прим. "Кофе: Эспрессо, цена: 27грн."
#
#   Store
#   - может импортировать продукты из файла invertory.csv
#   (по-умолчанию по 5 шт. каждого наименования)
#   - может вернуть список продуктов нужного типа (tea, coffee или все продукты)
#   - может вернуть общую стоимость продуктов в наличии
#   - может продать продукт
#*доп. Научить Store запоминать выручку(сумма проданных продуктов) и выводить баланс.
#Тип продукта может быть только coffee или tea (нельзя создать обьект с другим типом).

import sys

class Coffee:
    def __init__(self, coffee):
        self.name1 = []  # из файла
        self.type_1 = coffee = 5
        self.price = 0


class Tea:
    def __init__(self, tea):
        self.name1 = []  # из файла
        self.type_2 = tea = 5
        self.price = 0


class Shop:
    def __init__(self):
        self.ware_house = []  # из файла
        self.balance = 0.0
        self.transactions = []

    def sale(self):
        pass

    def __get__(self, instance, owner):
        pass

    def order(self):
        pass

    def balance_day(self):
        pass

a = Shop()
print(a)


