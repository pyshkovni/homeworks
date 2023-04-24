# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, 
# последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
a1 = len('Waste a Moment, Staying\' Alive,')
a2 = len('Waste a Moment, Staying\' Alive, A Sorta Fairytale,')
a3 = len('Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up,')
print(my_favorite_songs[:a1-1])
print(my_favorite_songs[a3+1:])
print(my_favorite_songs[a1+1:a2-1])
print(my_favorite_songs[a2+1:a3-1])