my_list = [2, 13, 18, 48, 215, 3, 4, 5]
#rezult=[2,0,18,48,0,0,4,0]
def nechet(my_list_arg):
    new_list = []
    my_count = 0
    for i in my_list_arg:
        if i % 2 != 0:
            my_count += 1
            new_list.append(0)
        else:
            new_list.append(i)
    print(new_list, my_count)
nechet(my_list)

