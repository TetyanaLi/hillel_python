#3. Написать функцию которая вернет самое длинное слово в строке:
# longest_word("What makes a good man") -> makes
#x = input('Введите действительное число с двумя знаками после десятичной точки: ')

some_list = str('What makes a good man')
elements = some_list.split()
 #def longest_word(elements[0:]):

#print(elements)
#print(len(elements))
new_list = []
for i in elements[0:]:
    new_list.append(len(i))
#print(new_list)
#print(max(new_list))
d = dict(zip(new_list,elements))
#print(d)
print(d.get(max(new_list)))

