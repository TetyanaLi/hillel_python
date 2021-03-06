#2. Написать программу которая будет форматировать номер телефона к единому виду.
#На ввод программа принимает строку введенного номера телефона, например:
#063-999-99-99 вывод (+38) 063 999-99-99
#063 999-99-99 вывод (+38) 063 999-99-99
#063-99999-99 вывод (+38) 063 999-99-99
#+3806399-999-99 вывод (+38) 063 999-99-99
#380639999999 вывод (+38) 063 999-99-99

#Если что-то не так с номером - пишет 'Failed to recognize number'.

import re
#string = input('Введите предполагаемый номер: ')


def check_tel_num(num):
    pattern = r'^[(]?[+]?(?:38){0,1}[)]?[- ]?([\d]{3})[- ]?([\d]{3})[- ]?([\d]{2})[- ]?([\d]{2})$'
    match = re.findall(pattern, num)
    try:
        (d1, d2, d3, d4) = re.findall(pattern, num)[0]
        return '(+38)' + ' ' + d1 + ' ' + d2 + '-' + d3 + '-' + d4
    except IndexError:
        return 'Failed to recognize number'


def main():
    string = input('Введите предполагаемый номер: ')
    print(check_tel_num(string))


if '__name__' == '__main__':
    main()