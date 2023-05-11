# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    _lst = ['Zero', 'One', 'Two', 'Tree', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return _lst[number]

try:
    _a = int(input('Введите число от 0 до 9   '))
    print(switch_it_up(_a))
except:
    print('вы ввели не правильное значение, введите целое число от 0 до 9')


