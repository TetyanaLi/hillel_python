# 2. Написать функцию которая определит является ли введенная строка палиндромом
# (та которая читается одинаково с любой стороны), пример:
# ШАЛАШ, КАЗАК, ДЕД, ДОХОД, 13231 и т.д.
#
some_string = str(input('Введите строку для проверки:  '))
new_string = some_string[::-1]


def palindrome(some_string, new_string):
    if some_string == new_string:
        return 'Верно!!! Введенная строка является ПАЛИНДРОМОМ!!!'
    else:
        return 'Введенная строка не является ПАЛИНДРОМОМ!!!'


print(palindrome(some_string, new_string))