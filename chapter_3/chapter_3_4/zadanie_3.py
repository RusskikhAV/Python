"""
        Рациональная считалочка

Напишите программу, которая производит счёт по заданным параметрам.

Формат ввода:
    В одну строку через пробел вводятся 3 рациональных числа — начало счета, конец и шаг.

Формат вывода:
    Последовательность чисел с заданными параметрами.
"""
from itertools import count
# разделяем строку по пробелу
string = input().split(' ')
# используя count библиотеки itertools назначаем начало отсчета цикла, шаг,
# соответствующими значениями из входной строки
# для value используем метод округления до двух знаков после запятой,
# далее пользуемся round_value
# если у нас после запятой меньше чем два знака, заполняем пустоты нулями
for value in count(float(string[0]), float(string[2])):
    round_value = round(value, 2)
    if round_value <= float(string[1]):
        if len(str(round_value)) < 4:
            print(str(round_value) + "0")
        else:
            print(round_value)
    else:
        break
