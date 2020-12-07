#1. Написать функцию `is_prime`, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую `True`, если оно простое, и `False` - иначе.
any_number = int(input('Введите любое число от 0 до 1000: '))
def is_prime(my_number):
    for i in range(2, my_number, 1):
        if my_number % i == 0:
            return False
    return True
#print(is_prime(any_number)) #1 вариант
new_rezult = is_prime(any_number)
print(new_rezult)






