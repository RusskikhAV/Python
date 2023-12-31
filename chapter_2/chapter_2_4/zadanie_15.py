"""
        Числовая змейка 2.0

Воспитательнице вновь нужна программа, которая будет генерировать змейку из чисел. Напишите программу,
которая строит числовую змейку требуемого размера.

Формат ввода:
    В первой строке записано число N — высота числового прямоугольника.
    Во второй строке указано число M — ширина числового прямоугольника.

Формат вывода:
    Нужно вывести сформированную числовую змейку требуемого размера.
    Чтобы прямоугольник был красивым, каждый его столбец следует сделать одинаковой ширины.
"""


# считывание и сохранение введенных с клавиатуры данных
n = int(input())
m = int(input())

# с помощью двойного цикла for по стороне n и по стороне m, после выходи из внутреннего цикла count = i
# и каждый раз когда j положительный меняю число по формуле (j * n) - (i - 1)
for i in range(1, n + 1):
    count = i
    for j in range(1, m + 1):
        if j % 2 == 0:
            print("".rjust(len(str(n * m)) - len(str((j * n) - (i - 1)))), (j * n) - (i - 1), sep="", end=" ")
        else:
            print("".rjust(len(str(n * m)) - len(str(count))), count, sep="", end=" ")
        count += n
    print()
