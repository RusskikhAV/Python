"""
        НОД

В одном из местных НИИ часто требуется находить наибольший общий делитель (НОД) двух чисел.
Вам уже доверяют, как одному из лучших «автоматизаторов» в округе, так что руководство НИИ решило заказать ПО у вас.

Формат ввода:
    Вводится два натуральных числа, каждое на своей строке.

Формат вывода:
    Требуется вывести одно натуральное число — НОД двух данных чисел.

Примечание
    Самый распространенный способ поиска НОД — алгоритм Евклида.
"""

a = int(input())
b = int(input())
while a != b:
    if a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
print(a)