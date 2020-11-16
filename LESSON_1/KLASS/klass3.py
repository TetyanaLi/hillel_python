some_list = []
some_text = ''
some_dict = {}

some_list.append('1')
some_list[0] = 20
some_text = '20'
some_list[0] = some_text
some_dict[some_text] = some_list

print(some_list, some_text, some_dict,sep='/')


