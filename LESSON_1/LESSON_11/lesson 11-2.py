#2. Написать функцию которая будет частично скрывать e-mail, пример:
#hide_email(somebody_email@gmail.com) -> em***@**il.com

some_list = str('somebody_email@gmail.com')

def hide_email (some_list):
    elements = some_list.split('@')
    print
    new_list = []
    for i in elements:
        new_list.append(len(i))
        d = dict(zip(new_list, elements))
        lw = d.get(max(new_list))
    return lw