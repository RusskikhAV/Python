"""
        Корень зла

Не все любят математику, а кто-то даже считает её настоящим злом во плоти, хотя от неё никуда не деться. К примеру,
Python изначально разрабатывался только для решения математических задач, поэтому давайте используем его,
 чтобы найти корни уравнения.

Формат ввода:
    Вводится 3 вещественных числа a, b, c — коэффициенты уравнения вида:
    ax ** 2 + bx + c = 0.

Формат вывода:
    Если у уравнения нет решений — следует вывести «No solution».
    Если корней конечное число — их нужно вывести через пробел в порядке возрастания с точностью до сотых.
    Если корней неограниченное число — следует вывести «Infinite solutions».

Примечание
Обратите внимание, что ограничения на значения коэффициентов отсутствуют.
"""

a = float(input())
b = float(input())
c = float(input())
x_1 = 0
x_2 = 0

discriminant = b ** 2 - 4 * a * c

if a == 0.0 and b == 0.0 and c == 0.0:
    print('Infinite solutions')
elif a == 0.0 and b == 0.0:
    print('No solution')
else:
    if a == 0.0:
        x = -c / b
        print("{:.2f}".format(x))
        if b == 0.0 and c == 0.0:
            print("{:.2f}".format(round(0, 2)))
        if a != 0.0 and b == 0.0 and c != 0.0:
            if ((- c) / a) < 0:
                print('No solution')
            elif ((-c) / a) > 0:
                agg = abs(c / a) ** 0.5
                ag = agg
                ag2 = -agg
                afk = min(ag, ag2)
                afk2 = max(ag, ag2)
                print(round(afk, 2), round(afk2, 2))
        if a != 0.0 and b != 0.0 and c == 0.0:
            print("{:.2f}".format(0), "{:.2f}".format(round((-b / a), 2)))
    if a == 0.0 and b != 0.0:
        print("{(-c) / b:.2f}")
    elif discriminant >= 0.0 and a != 0.0:
        x_1 = ((-b) + discriminant ** 0.5) / (2 * a)
        x_2 = ((-b) - discriminant ** 0.5) / (2 * a)
        if x_1 == x_2:
            print("{:.2f}".format(x_1))
        else:
            if x_1 < x_2:
                print("{:.2f} {:.2f}".format(x_1, x_2))
            else:
                print("{:.2f} {:.2f}".format(x_2, x_1))
    else:
        print('No solution')
