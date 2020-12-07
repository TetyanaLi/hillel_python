#1. Написать функцию которая посчитает количество очков футбольной команды.
# Победа дает 3 очка, ничья 1 очко, поражение 0 очков.
# Функция принимает три аргумента - win, draw, loss.
# Пример : count_points(3, 2, 2) -> 11

win = int(input())
draw = int(input())
loss = int(input())
def count_points(win, draw, loss):
    summ_coint = (win * 3) + (draw * 1) + (loss * 0)  # loss не влияет на результат
    return summ_coint
print(count_points(win, draw, loss))