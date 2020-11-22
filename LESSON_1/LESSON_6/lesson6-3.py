
#3. Дан список значений. Вернуть словарь где каждый ключ - это индекс листа,
#   а значение листа - это значение ключа:
#   Input:
my_list = ['a', 'b', 'c', 'd', 'e']
#   Output
#   {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
new_dict={}
for element in my_list:
    new_idx = my_list.index(element)
    new_dict[new_idx]=element
print(new_dict) # ВАРИАНТ 1

index_list = range(len(my_list))
print(dict(zip(index_list, my_list ))) # ВАРИАНТ 2


