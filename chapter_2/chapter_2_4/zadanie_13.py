"""
        Числовой прямоугольник 2.0

Давайте вновь поможем воспитательнице учить ребят числам. Напишите программу,
которая строит числовой прямоугольник требуемого размера.

Формат ввода:
    В первой строке записано число N — высота числового прямоугольника.
    Во второй строке указано число M — ширина числового прямоугольника.

Формат вывода:
    Нужно вывести сформированный числовой прямоугольник требуемого размера.
    Чтобы прямоугольник был красивым, каждый его столбец должен обладать одинаковой шириной.
"""

# считывание и сохранение введенных с клавиатуры данных
n = int(input())
m = int(input())

# с помощью двойного цикла for по стороне n и по стороне m, вывожу count увеличивая на n каждый раз за итерацию
# при выходе из внутреннего цикла count = i
for i in range(1, n + 1):
    count = i
    for j in range(m):
        print("".rjust(len(str(n * m)) - len(str(count))), count, sep="", end=" ")
        count += n
    print()