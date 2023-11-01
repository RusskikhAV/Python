"""
        Красота спасёт мир

Одно из древних поверий гласит, что трёхзначное число красиво,
если сумма его минимальной и максимальной цифр равна оставшейся цифре умноженной на 2.

Напишите систему определяющую красоту числа.

Формат ввода
    Одно трёхзначное число

Формат вывода
    YES — если число красивое, иначе — NO
"""

number = input()

max_number = max(number[::])
min_number = min(number[::])
last_number = list(number[::])
index_max = number.find(max_number)
index_min = number.find(min_number)
if index_max > index_min:
    last_number.pop(index_max)
    last_number.pop(index_min)
else:
    last_number.pop(index_min)
    last_number.pop(index_max)

if int(max_number) + int(min_number) == int(last_number[0]) * 2:
    print("YES")
else:
    print("NO")
