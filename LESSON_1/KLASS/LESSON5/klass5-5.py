some_list = [10, 20, 30, 40, 5]
some_text = ''
some_dict = {}

some_list[0] = 20
some_text = '20'
some_dict[some_text] = some_list

print(some_list)
some_list.sort()
print(some_list)
del some_list[0]
print(some_list)  #сортировка и удаление элемента с индексом 0