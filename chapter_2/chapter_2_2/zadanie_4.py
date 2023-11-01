"""
        Список победителей

Длина трассы — 43872м, и зрители хотят узнать имя победителя.

Нам известны средние скорости трёх фаворитов – Пети, Васи и Толи. Помогите подвести итоги гонки.

Формат ввода
    В первой строке записана средняя скорость Пети.
    Во второй — Васи.
    В третьей — Толи.

Формат вывода
    Имена победителей в порядке занятых мест.
"""

average_speed_1 = int(input())
average_speed_2 = int(input())
average_speed_3 = int(input())

name_1_place = ""
name_2_place = ""
name_3_place = ""

first_competitor = "Петя"
second_competitor = "Вася"
third_competitor = "Толя"

if average_speed_2 < average_speed_1 > average_speed_3:
    name_1_place = first_competitor
elif average_speed_2 < average_speed_1 < average_speed_3 or average_speed_2 > average_speed_1 > average_speed_3:
    name_2_place = first_competitor
else:
    name_3_place = first_competitor

if average_speed_1 < average_speed_2 > average_speed_3:
    name_1_place = second_competitor
elif average_speed_1 < average_speed_2 < average_speed_3 or average_speed_1 > average_speed_2 > average_speed_3:
    name_2_place = second_competitor
else:
    name_3_place = second_competitor

if average_speed_1 < average_speed_3 > average_speed_2:
    name_1_place = third_competitor
elif average_speed_1 > average_speed_3 > average_speed_2 or average_speed_1 < average_speed_3 < average_speed_2:
    name_2_place = third_competitor
else:
    name_3_place = third_competitor

print("1. ", name_1_place, "\n", "2. ", name_2_place, "\n", "3. ", name_3_place, "\n", sep="")
