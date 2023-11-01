"""
        Властелин Чисел: Две Башни

Во времена, когда люди верили в великую силу чисел, оказалось,
что волшебник Пифуман предал все народы и стал помогать Зерону.
Чтобы посетить башни обоих злодеев одновременно, нам следует разделить магию числа, которое защищало нас в дороге.

Чтобы поделить трёхзначное число, нам нужно составить из него минимально и максимально возможные двухзначные числа.

Формат ввода
    Одно трёхзначное число.

Формат вывода
    Два защитных числа для каждого отряда, записанные через пробел.
"""

number_1 = list(input())
number_2 = number_1

number_for_first_squad = ""
number_for_second_squad = ""

min_num_1 = min(number_1)
index_min_num_1 = number_1.index(min_num_1)
number_1.pop(index_min_num_1)
min_num_2 = min(number_1)

if int(min_num_1) == 0:
    number_for_first_squad += min_num_2
    number_for_first_squad += min_num_1
else:
    number_for_first_squad += min_num_1
    number_for_first_squad += min_num_2

max_num_1 = max(number_2)
index_max_num_1 = number_2.index(max_num_1)
number_2.pop(index_max_num_1)
max_num_2 = max(number_2)

number_for_second_squad += max_num_1
number_for_second_squad += max_num_2

print(number_for_first_squad, number_for_second_squad)
