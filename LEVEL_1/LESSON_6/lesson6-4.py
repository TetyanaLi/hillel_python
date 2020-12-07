
#4. Во вложении есть json файл. Написать программу которая прочитает его и посчитает общую длительность всех треков в альбоме.
#Базовый кейс - вернет количество секунд.
#   * доп. усложнение вернуть в виде строки часы:минуты:секунды, прим. '0:41:39' (datetime.timedelta)

import json
path = 'acdc.json'
with open(path,'r') as f:
    data = json.loads(f.read())
    duration_list=[int(track['duration']) for track in
                   data['album']['tracks']['track']]
    print(duration_list)
    print(sum(duration_list))



#  duration = 0
#   for track in data['album']['tracks']['track']:
#        duration += int(track['duration'])
#print(duration)