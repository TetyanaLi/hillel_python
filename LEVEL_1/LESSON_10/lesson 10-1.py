# 1. Программа которая при запуске должна:
#  Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
#  Окончанием ввода пусть служит
# пустая строка. Каждая введённая строка, в файле, должна начинаться с новой строки.
#
text_file = open('new_text.txt', 'w')

while True:
    some_text = input('Введите текст или нажмите Enter для выхода: ')
    if some_text != '':
        text_file.write(some_text+'\n')
    if some_text == '':
        print('Запись файла завершена.')
        break

text_file.close()