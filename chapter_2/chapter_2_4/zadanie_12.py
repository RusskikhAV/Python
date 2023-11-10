"""
        Числовой прямоугольник

Ребята в детском саду учатся считать, и чтобы им было интереснее, воспитательница решила оформить список изучаемых
чисел особым образом. Дети справляются весьма быстро, поэтому ей требуется программа способная строить числовые
прямоугольники. Напишите программу, которая строит числовой прямоугольник требуемого размера.

Формат ввода:
    В первой строке записано число N — высота числового прямоугольника.
    Во второй строке указано число M — ширина числового прямоугольника.

Формат вывода:
    Нужно вывести сформированный числовой прямоугольник требуемого размера.
    Чтобы прямоугольник был красивым, каждый его столбец должен быть одинаковой ширины.
"""

# считывание и сохранение введенных с клавиатуры данных
n = int(input())
m = int(input())

count = 1

# с помощью двойного цикла for по стороне n и по стороне m, вывожу count увеличивая каждый раз за итерацию
for i in range(n):
    for j in range(m):
        print("".rjust(len(str(n * m)) - len(str(count))), count, sep="", end=" ")
        count += 1
    print()