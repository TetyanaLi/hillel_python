#3.Получить прогноз погоды для Одессы на следующие 5 дней и записать в файл с именем текущей даты,
#http: // api.openweathermap.org / data / 2.5 / forecast / daily?q = city & cnt = 1 & units = metric & appid =
# f9ada9efec6a3934dad5f30068fdcbb8
#Параметр cnt = количество дней
#Параметр q = город
#Так мы получим и обработаем дату из ответа(ключ dt):
#datetime.datetime.fromtimestamp(1600419600)
#Применив к полученному обьекту даты strftime("%d-%m-%Y") получим строковую дату для записи в файл.

#Пример имени файла:
# 19 - 09 - 2020 - Odessa - 5 - days - weather - forecast.txt
#Записанный файл должен выглядеть вот так:
#Дата                 Температура днем                По ощущениям
#18 - 09 - 2020              17.86                        11.18
#19 - 09 - 2020              15.75                        11.21
#20 - 09 - 2020              20.37                        17.49
#21 - 09 - 2020              20.75                        18.08
#22 - 09 - 2020              20.96                        17.47

#*доп.предоставить пользователю выбор города и количества дней, а также добавить колонку Температура ночью

import datetime
import requests
URL = 'http://api.openweathermap.org/data/2.5/forecast/daily'

#user_input_city = input('Enter city: ') # С ГОРОДОМ не ПОЛУЧАЕТСЯ пока
user_input_count = int(input('Enter count: '))

def return_weather(days=1):
    data = {'q': 'Odesa', 'cnt': days, 'units': 'metric','appid': 'f9ada9efec6a3934dad5f30068fdcbb8'}
    r = requests.get(URL, data)
    return r.json()
result = return_weather (user_input_count)

print('Дата\t\tTемпература днем\tПо ощущениям днем\tТемпература ночью\tПо ощущениям ночью')
for day in result['list']:
    data = day['dt']
    print(str(datetime.datetime.fromtimestamp(data).strftime("%d-%m-%Y")), '\t'*2, str(day['temp']['day']),
          '\t' * 4, str(day['feels_like']['day']), '\t'*5, str(day['temp']['night']), '\t'*4,
          str(day['feels_like']['night']))

name_of_file = str(datetime.datetime.today().strftime("%d-%m-%Y")) + '-Odessa-' + str(user_input_count) + '-days-forecast.txt'
with open(name_of_file ,'w') as f:
    f.writelines('Дата\t\tTемпература днем\tПо ощущениям днем\tТемпература ночью\tПо ощущениям ночью'+'\n')
    for day in result['list']:
        data = day['dt']
        f.writelines(str(datetime.datetime.fromtimestamp(data).strftime("%d-%m-%Y"))+'\t' * 2 + str(day['temp']['day'])
                          + '\t' * 4 + str(day['feels_like']['day']) + '\t' * 5 + str(day['temp']['night'])
                          + '\t' * 4 + str(day['feels_like']['night']) + '\n')

