#2. Написать функцию которая возвращает текущее время. И обернуть ее в декоратор @countdown
#  который отсчитает 3 секунды.
#  Пример:
#  >>> what_time_is_it_now()
#  3
#  2
#  1
#  '16:21'
#time.sleep() поможет программе уснуть на первый аргумент секунду =)
#  Вернуть время поможет метод time.strftime, с аргументом '%H:%M'


#import datetime
#now_time =datetime.datetime.now()
#now_time_str = now_time.strftime('what_time_is_it_now? ''%H:%M:%S')
#kjkjprint (now_time_str)

#def countdown(func):
#    import time
#    def seconds():
#        time.sleep(1)
#        print(3)
#        time.sleep(1)
#        print(2)
#        time.sleep(1)
#        print(1)
#        func()
#    return seconds # вариант 1

def countdown(func):
    import time
    def seconds(*args):
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        func(*args)
    return seconds  # вариант 2

@countdown
def time_now():
    import time
    print(time.strftime('%H:%M', time.localtime()))
#def return_name(name):
#    return name
#print(return_name (input('Enter name:  ')))
print("What time is now?")
time_now()

