#5. Дана строка.
#   a. выведите третий символ этой строки.
#   b. выведите предпоследний символ этой строки.
#   c. выведите первые пять символов этой строки.
#   d. выведите всю строку, кроме последних двух символов.
#   e. выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная
#   с первого).
#   f. выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
#   g. выведите все символы в обратном порядке.
#   h. выведите все символы строки через один в обратном порядке, начиная с последнего.
#   i. выведите длину данной строки.

some_text = list(input('Введите текст: '))  # ВАРИАНТ 1 можно не использовать list, но тогда не видно пробелов
print(some_text[2])
print(some_text[-2])
print(some_text[0:5])
print(some_text[:-2])
print(some_text[2::2])
print(some_text[1::2])
print(some_text[::-1])
print(some_text[::-2])
print(len(some_text))

some_text = input('Введите текст: ')  # ВАРИАНТ 2
print(some_text[2])
print(some_text[-2])
print(some_text[0:5])
print(some_text[:-2])
print(some_text[2::2])
print(some_text[1::2])
print(some_text[::-1])
print(some_text[::-2])
print(len(some_text))