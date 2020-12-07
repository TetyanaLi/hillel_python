#3. Написать функцию которая вернет самое длинное слово в строке:
# longest_word("What makes a good man") -> makes
#x = input('Введите действительное число с двумя знаками после десятичной точки: ')

some_list = str('What makes a good man')
def longest_word(some_list):
    elements = some_list.split()
    new_list = []
    for i in elements:
        new_list.append(len(i))
        d = dict(zip(new_list, elements))
        lw = d.get(max(new_list))
    return lw
print(longest_word(some_list)) # 1 ВАРИАНТ

def longest_word(some_list):
    elements = {len(val): val for val in some_list.split()}
    return elements[max(elements)]
some_list = str('What makes a good man')
print(longest_word(some_list))  # 2 ВАРИАНТ

def longest_word(some_string):
    return max(some_string.split(), key=len)
some_list = str('What makes a good man')
print(longest_word(some_list))  # 3 ВАРИАНТ















#some_list = str('What makes a good man')
#elements = some_list.split()
 #def longest_word(elements[0:]):

#print(elements)
#print(len(elements))
#new_list = []
#for i in elements:
#    new_list.append(len(i))
#print(new_list)
#print(max(new_list))
#d = dict(zip(new_list,elements))
#print(d)
#print(d.get(max(new_list)))





