x=float(input('Введите любое число: '))
a=(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
if abs(x) in a:
    print('Это число есть в списке.')
else:
    print('Этого числа нет в списке')