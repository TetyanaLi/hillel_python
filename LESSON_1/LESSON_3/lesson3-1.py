#1. Пользователь вводит трехзначное число. Найдите сумму его цифр.
any_number = input('Введите трехзначное число: ')
result = int(any_number[0]) + int(any_number[1]) + int(any_number[2])
print(result) #ВАРИАНТ 1

s_m = 0
for i in any_number:
    s_m += int(i)
print(s_m) # ВАРИАНТ 2

