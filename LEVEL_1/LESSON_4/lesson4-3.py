#3. Даны два целых числа `A` и `В`. Выведите все числа от `A` до `B` включительно,
# в порядке возрастания, если `A < B`, или в порядке убывания в противном случае.

number_1 = int(input('введите целое число - '))
number_2 = int(input('введите целое число - '))
if number_1 < number_2:
    numbers = list(range(number_1, number_2 + 1))
    print(numbers)
elif number_2 < number_1:
    numbers = list(range(number_1, number_2 - 1, -1))
    print(numbers)
else:
    print('Ошибка ввода!!!')

