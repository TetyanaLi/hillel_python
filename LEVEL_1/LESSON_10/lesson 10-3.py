# 3. Написать функцию которая сдвинет полученный список на N элементов вправо или влево,
# принимаемые аргументы - список и натуральное число(если отрицательное сдвигаем влево, положительное - вправо).

list_numb = list(map(int, input('Введите ряд чисел через пробел: ').split()))
shift_numb = int(input('Введите натуральное число для сдвига: '))


def shift_numbers(shifted_numbs, func_shift):
    shifted_numbs = shifted_numbs[-func_shift:] + shifted_numbs[:-func_shift]
    return shifted_numbs


print(shift_numbers(list_numb, shift_numb))
