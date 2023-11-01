"""
        Легенды велогонок возвращаются: кто быстрее?

В новом сезоне за первенство в велогонках вновь борются лучшие из лучших. Протяжённость заключительной трассы — 43872м,
 и все хотят знать, кто получит золотую медаль.

Нам известны средние скорости трёх претендентов на победу – Пети, Васи и Толи. Кто из них победит?

Формат ввода
    В первой строке записана средняя скорость Пети.
    Во второй — Васи.
    В третьей — Толи.

Формат вывода
    Красивый пьедестал (ширина ступеней 8 символов).
"""

speed_petya = int(input())
speed_vasya = int(input())
speed_tolya = int(input())

name_vasya = "Вася"
name_petya = "Петя"
name_tolya = "Толя"

name_1_place = ""
name_2_place = ""
name_3_place = ""

if speed_tolya < speed_petya > speed_vasya:
    name_1_place = name_petya
    if speed_tolya > speed_vasya:
        name_2_place = name_tolya
        name_3_place = name_vasya
    else:
        name_2_place = name_vasya
        name_3_place = name_tolya
elif speed_tolya < speed_vasya > speed_petya:
    name_1_place = name_vasya
    if speed_tolya > speed_petya:
        name_2_place = name_tolya
        name_3_place = name_petya
    else:
        name_2_place = name_petya
        name_3_place = name_tolya
else:
    name_1_place = name_tolya
    if speed_vasya > speed_petya:
        name_2_place = name_vasya
        name_3_place = name_petya
    else:
        name_2_place = name_petya
        name_3_place = name_vasya
print("{:>14}\n"
      "{:>6}\n"
      "{:>22}\n"
      "   II      I      III   "
      .format(name_1_place, name_2_place, name_3_place))
