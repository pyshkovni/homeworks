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

import random
from datetime import timedelta
import math

while True:                                                 #Исключим повторение песен
    song1 = random.choice(my_favorite_songs)
    song2 = random.choice(my_favorite_songs)
    song3 = random.choice(my_favorite_songs)
    if song1 != song2 and song2 != song3 and song1 != song3:
        break
songs = song1 [0] +", " + song2 [0] + ", " + song3 [0]        #Определим список песен
t1 = math.modf(song1 [1])                                     #Определим время звучания
t2 = math.modf(song2 [1])
t3 = math.modf(song3 [1])
time = timedelta(minutes = t1[1], seconds = t1[0] * 100 ) + timedelta(minutes = t2[1], seconds = t2[0] * 100 ) + timedelta(minutes = t3[1], seconds = t3[0] * 100 )
print("Выбраны песни", songs, "и они звучат", time)

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

while True:                                                 #Исключим повторение песен
    song1 = key1, val1 = random.choice(list(my_favorite_songs_dict.items()))
    song2 = key2, val2 = random.choice(list(my_favorite_songs_dict.items()))
    song3 = key3, val3 = random.choice(list(my_favorite_songs_dict.items()))
    if song1 != song2 and song2 != song3 and song1 != song3:
        break
songs = key1 +", " + key2 + ", " + key3        #Определим список песен
t1 = math.modf(val1)                           #Определим время звучания
t2 = math.modf(val2)
t3 = math.modf(val3)
t = timedelta(minutes = t1[1], seconds = t1[0] * 100 ) + timedelta(minutes = t2[1], seconds = t2[0] * 100 ) + timedelta(minutes = t3[1], seconds = t3[0] * 100 )
print("Из словаря выбраны песни", songs, "и они звучат", t)

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
