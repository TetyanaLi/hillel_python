some_list = [10, 20, 30, 40, 5]
some_text = ''
some_dict = {}

some_list[0] = 20
some_text = '20'
some_dict[some_text] = some_list

print(some_list)
some_list.sort() #сортировка списка
print(some_list)
del some_list[0] #удаление элемента с индексом 0
print(some_list)
some_list.pop() #удаление последнего элемента (ПО ИНДЕКСУ)
print(some_list)
some_list.remove(20) #удаление по значению
print(some_list)
print(some_list.index(30))
print(some_list)
# some_list.clear() одно и тоже some_list=[] очистка списка