a = float(input('Введите величину стороны квадрата:'))
def square (a):
    p = a * 4
    s = a ** 2
    d = (2 * a ** 2) ** 0.5
    rezult = (p, s, d)
    return rezult
print(square(a))
