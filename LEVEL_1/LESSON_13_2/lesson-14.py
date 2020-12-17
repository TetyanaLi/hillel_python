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

class Product:

    def __init__(self, product_name, product_type, price):
        self.product_name = product_name
        self.product_type = self._check_product_type(product_type)  # тут функция которая вернет
        self.price = float(price)                                   # чай или кофе или None если другое например

class Store:

    def __init__(self):
        self.ware_house = []  # из файла
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


