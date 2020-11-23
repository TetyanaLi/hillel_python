#5. Пользователь вводит число от 1 до 10, программа генерирует рандомное число от 1 до 10,
# если числа равны напечатать 'You won!' если нет - 'You lose!'. Дать пользователю три попытки ;)
number=int(input('Введите число от 1 до 10: '))
import random
any_number=(random.randint(1, 10))
if number==any_number:
    print('You won!')
else:
    print('You lose!')