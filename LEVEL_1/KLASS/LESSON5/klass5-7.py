some_list = [10, 20, 30, 40, 5]
some_text = ''
some_dict = {}

some_list[0] = 20
some_text = '20'
some_dict[some_text] = some_list

some_list = [[1, 2, 3] , [4, 5, 6]]
some_list2 = some_list.copy()
some_list2[0].append(4)
print(some_list)