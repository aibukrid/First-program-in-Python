#my_name = input('Введите Ваше имя: ')
#year = input('Введите какой сейчас год: ')
#year_of_birth=input('Введите Ваш год рождения: ')
#age = (int(year)-int(year_of_birth))
#print('Меня зовут:',my_name,'.''\n''Сейчас идёт',year,'год.''\n''Я родился в',year_of_birth,'.''\n''Мне',age,'.')

from math import ceil
time = input('Сколько минут прошло с начала дня: ')
h = (int(time) // 60)
a = (int(time) / 60 - h)
min: int = ceil(a)
print(h,':',min)