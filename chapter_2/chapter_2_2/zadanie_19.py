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

attention = 'Опасность! Покиньте зону как можно скорее!'
normal = "Зона безопасна. Продолжайте работу."
ocean = "Вы вышли в море и рискуете быть съеденным акулой!"

x = float(input())
y = float(input())
if (x ** 2 + y ** 2) ** 0.5 > 10:
    print(ocean)
elif x >= 0 and y >= 0 and (x ** 2 + y ** 2) ** 0.5 <= 5:
    print(attention)
elif -4 <= x < 0 <= y <= 5:
    print(attention)
elif -7 <= x < -4 and 5 >= y >= 0 and 5 * x - 3 * y > -35:
    print(attention)
elif 0.25 * x ** 2 + 0.5 * x - 8.75 <= y <= 0:
    print(attention)
else:
    print(normal)
