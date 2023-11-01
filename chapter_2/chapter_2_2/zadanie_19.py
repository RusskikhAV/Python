"""
Автоматизация безопасности
Группа исследователей собирается высадиться на остров невероятно ровной формы, но разведка при помощи спутника выяснила,
 что на острове есть зона зыбучих песков.

Для повышения безопасности экспедиции было решено разработать систему оповещения, которая предупредит исследователей об
опасности. А для снижения расходов на производство было решено заказать программное обеспечение.

Схема (смотри схему: .docs/img/schema.png)

Напишите программу, которая по координатам исследователя, будет сообщать о безопасности в этой точке.

Формат ввода
    Два рациональных числа — координаты исследователя.

Формат вывода
    Одно из сообщений:
        - Опасность! Покиньте зону как можно скорее!
        - она безопасна. Продолжайте работу.
        - Вы вышли в море и рискуете быть съеденным акулой!
"""

import math

a = float(input())
b = float(input())

attention = 'Опасность! Покиньте зону как можно скорее!'
normal = "Зона безопасна. Продолжайте работу."
ocean = "Вы вышли в море и рискуете быть съеденным акулой!"


# вычисление положения точки, через сумму векторов в треугольнике
def sum_vectors(px, py):
    ax = 0
    ay = 0
    bx = 0
    by = 5
    cx = -3
    cy = 0

    # AB
    abx = bx - ax
    aby = by - ay

    # AP = {px - ax, py - ay, pz - az}
    apx = px - ax
    apy = py - ay

    # a × b = {ay * bz - az * by ; az * bx - ax * bz ; ax * by - ay * bx}.
    # ABxAP = {aby * apz - abz * apy, abz * apx - abx * apz, abx * apy - aby * apx}
    k_ab_ap = abx * apy - aby * apx

    # BC
    bcx = cx - bx
    bcy = cy - by

    # BP
    bpx = px - bx
    bpy = py - by

    # BCxBP
    k_bc_bp = bcx * bpy - bcy * bpx

    # CA
    acx = ax - cx
    acy = ay - cy

    # CP
    cpx = px - cx
    cpy = py - cy

    # CAxCP
    k_ca_cp = acx * cpy - acy * cpx

    return k_ab_ap, k_bc_bp, k_ca_cp


# за пределами острова?
if -10 >= a or 10 <= a or -10 >= b or 10 <= b:
    r = 10
    h = math.sqrt(a ** 2 + b ** 2)
    if h >= r:
        print(ocean)
    else:
        print(normal)

# для X Y
elif a >= 0 and b >= 0:
    r = 5
    h = math.sqrt(a ** 2 + b ** 2)
    if h <= r:
        print(attention)
    else:
        print(normal)
# для -X Y
elif a <= 0 <= b:
    if a >= -4 and b <= 5:
        print(attention)
    elif -7 <= a <= -4:
        a1 = a + 4
        if 5 >= b >= 0 >= a1 >= -3:
            s = sum_vectors(a1, b)
            if s[0] > 0 and s[1] > 0 and s[2] > 0:
                print(attention)
            elif s[0] < 0 and s[1] < 0 and s[2] < 0:
                print(attention)
            elif s[0] == 0 or s[1] == 0 or s[2] == 0:
                if s[0] == 0:
                    if (s[1] > 0 and s[2] > 0) or (s[1] < 0 and s[2] < 0):
                        print(attention)
                if s[1] == 0:
                    if (s[0] > 0 and s[2] > 0) or (s[0] < 0 and s[2] < 0):
                        print(attention)
                if s[2] == 0:
                    if (s[1] > 0 and s[0] > 0) or (s[1] < 0 and s[0] < 0):
                        print(attention)
            else:
                print(normal)
        else:
            print(normal)
    else:
        print(normal)

# 9*sin(x/4−4/3) or y=\ -9*cos((x / 3.819) + 0.25)
# для X -Y & для -Х -Y
elif (a >= 0 >= a) or b <= 0:
    # y = 9.01 * math.sin((a / 3.85) - (27.5 / 21))
    y = -9.02 * math.cos((a / 3.819) + 0.25)
    if y <= b:
        print(attention)
    else:
        print(normal)
