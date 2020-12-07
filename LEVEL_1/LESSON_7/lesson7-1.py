#1. Написать функцию которая вернет строку введенную пользователем.
#  Обернуть функцию в декоратор чтобы функция вместо строки целиком вернула список слов.
def new_list(function):
    func = function()
    print(func.split())
    return func

@new_list
def user_list():
    return input('Введите что-нибудь: ')

