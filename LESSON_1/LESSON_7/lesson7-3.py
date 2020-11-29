#3.Получить прогноз погоды для Одессы на следующие 5 дней и записать в файл с именем текущей даты,
#http: // api.openweathermap.org / data / 2.5 / forecast / daily?q = city & cnt = 1 & units = metric & appid =
# f9ada9efec6a3934dad5f30068fdcbb8
#Параметр cnt = количество дней
#Параметр q = город
#Так мы получим и обработаем дату из ответа(ключ dt):
#datetime.datetime.fromtimestamp(1600419600)
#Применив к полученному обьекту даты strftime("%d-%m-%Y") получим строковую дату для записи вфайл.

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

import requests
URL='http://api.openweathermap.org/data/2.5/forecast/daily'
def return_weather(days=1):
    data = {'q' : 'Odesa','cnt' : days, 'units':'metric','appid':'f9ada9efec6a3934dad5f30068fdcbb8'}
    r = requests.get(URL, data)
    return r.json()
result = return_weather(days = 5)
def write_file():
    prin
print('Tемпература днем\tТемпература ночью\tПо ощущениям днем\tПо ощущениям ночью')
#print(result)
for day in result['list']:
   print('\t', day['temp']['day'],'\t' * 4, day['feels_like']['day'],
         '\t' *5 , day['temp']['night'],'\t'*4, day['feels_like']['night'])
print('done')

import datetime
print(datetime.datetime.today())
