my_list = [2, 13, 18, 48, 215, 3, 4, 5]
#rezult=[2,0,18,48,0,0,4,0]
def nechet(my_list_arg):
    my_count = 0
    for index in range(len(my_list_arg)):
        number = my_list_arg[index]
        if number % 2 != 0:
            my_count = my_count + 1
            my_list_arg[index] = 0
    print(my_list_arg, my_count)
nechet(my_list)
