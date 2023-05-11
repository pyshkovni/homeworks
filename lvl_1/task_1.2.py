# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random, datetime
a = random.randint(0,8)
b = random.randint(0,8)
c = random.randint(0,8)
time_sum_A = (my_favorite_songs[a][1]) + (my_favorite_songs[b][1]) + (my_favorite_songs[c][1])
print(f'Три песни звучат {time_sum_A} минут ')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
import random
key_list = list(my_favorite_songs_dict.keys()) # преобразование ключей в список
key1, key2, key3 = random.sample(key_list, 3) # выбор из списки 3-х произвольных значений
time_sum_B = my_favorite_songs_dict[key1] + my_favorite_songs_dict[key2] + my_favorite_songs_dict[key3] #  по ключу достаем время в словаре и суммируем с другими  
#print(key1, ',',  key2, ',', key3)
print(f'Три песни звучат {time_sum_B} минут.')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Выполнено

# Если дополнительно вас интересуют пункты  С и D, то они были выполнены следующим образом
# Импорты
from random import sample
from datetime import timedelta
from math import modf

# Пункт D(А)
total_time = timedelta()
for song in sample(my_favorite_songs, 3):
    s, m = modf(song[1])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Пункт D(A): Три песни звучат {total_time}')

# Пункт D(B)
total_time = timedelta()
for song in sample(tuple(my_favorite_songs_dict), 3):
    s, m = modf(my_favorite_songs_dict[song])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Пункт D(B): Три песни звучат {total_time}')
