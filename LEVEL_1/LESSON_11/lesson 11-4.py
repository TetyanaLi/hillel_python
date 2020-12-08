#4. Написать функцию которая заменит в тексте слово на другое.
#  Функция принимает 4 аргумента, изначальная строка, заменяемое слово, новое слово, количество замен, пример:
#  fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel',
#  1) -> 'Marvel makes good movies, DC makes good comics'
#  fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel',
#  2) -> 'Marvel makes good movies, Marvel makes good comics'

def text_replacement(start_string, word, new_word, number_of_replacement):
    new_string = start_string.replace(word, new_word, number_of_replacement)
    return new_string

fake_string = 'DC makes good movies,DC makes good comics'
number_of_repl = int(input('Количество замен: '))
print(text_replacement(fake_string, 'DC', 'Marvel', number_of_repl))