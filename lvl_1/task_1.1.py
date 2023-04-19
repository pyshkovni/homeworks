# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

first = my_favorite_songs.split(',')[0]
second = my_favorite_songs.split(',') [1]
last = my_favorite_songs.split(',') [-1]
prelast = my_favorite_songs.split(',') [-2]
print(first, last, second, prelast)