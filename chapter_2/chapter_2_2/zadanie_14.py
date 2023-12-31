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

# считывание и сохранение введенных с клавиатуры данных, а так же дублирую
number_1 = list(input())
number_2 = number_1

number_for_first_squad = ""
number_for_second_squad = ""

# нахожу две минимальных цифры и числа
min_num_1 = min(number_1)
index_min_num_1 = number_1.index(min_num_1)
number_1.pop(index_min_num_1)
min_num_2 = min(number_1)

# проверяю, не является ли минимальная цифра 0, и составляю минимальные числа
if int(min_num_1) == 0:
    number_for_first_squad += min_num_2
    number_for_first_squad += min_num_1
else:
    number_for_first_squad += min_num_1
    number_for_first_squad += min_num_2

# нахожу две максимальные цифры и числа
max_num_1 = max(number_2)
index_max_num_1 = number_2.index(max_num_1)
number_2.pop(index_max_num_1)
max_num_2 = max(number_2)

# составлю максимальное число
number_for_second_squad += max_num_1
number_for_second_squad += max_num_2

# вывод двух составленных чисел в консоль
print(number_for_first_squad, number_for_second_squad)
