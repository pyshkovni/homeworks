# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

# Создание списка целых чисел
import random
_lst = []
for _ in range(10):
    _lst.append(random.randint(-1000, 1000))


def minimum(arr):
    _a = arr[0]
    _b = 0
    for _ in arr:
        if arr[_b] < _a:
            _a = arr[_b]
        _b += 1
    return _a

        
def maximum(arr):
    _a = arr[0]
    _b = 0
    for _ in arr:
        if arr[_b] > _a:
            _a = arr[_b]
        _b += 1
    return _a


print(f'Список {_lst}, минимум: {minimum(_lst)}, максимум: {maximum(_lst)}')

# Отлично! Вот, например, вариант через быструю сортировку

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def maximum(arr):
    return quicksort(arr)[-1]

def minimum(arr):
    return quicksort(arr)[0]

print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))
