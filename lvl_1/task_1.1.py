# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, 
# последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

_a = ','
_lst = []
for _index, _char in enumerate(my_favorite_songs):
    if _char == _a:
        _lst.append(_index)

print(my_favorite_songs[:_lst[0]])
print(my_favorite_songs[_lst[3]+2:])
print(my_favorite_songs[_lst[0]+2 : _lst[1]])
print(my_favorite_songs[_lst[2]+2 : _lst[3]])
