"""
        Кашееды

Каждый воспитанник детского сада любит либо манную, либо овсяную, либо обе каши.
Давайте создадим программу, которая позволит воспитателю быстро выяснить, сколько детей любят обе каши.

Формат ввода:
    В первых двух строках указывается количество детей, любящих манную и овсяную каши (N и M).
    Затем идут N строк — фамилии детей, которые любят манную кашу, и M строк с фамилиями детей, любящих овсяную кашу.
    Гарантируется, что в группе нет однофамильцев.

Формат вывода:
    Количество учеников, которые любят обе каши.
    Если таких не окажется, в строке вывода нужно написать «Таких нет».
"""

# считываем с клавиатуры количество любителей манной каши и овсяной
n, m = int(input()), int(input())
# создаём два множества, в каждом из них будет храниться информация о фамилии кашееда
set_1, set_2 = set(), set()
# в цикле считываем фамилии и добавляем их в множество
for i in range(n):
    set_1.add(input())

for i in range(m):
    set_2.add(input())
# находим пересечение множеств и выводим его длину, если длина не равна нулю, иначе "Таких нет"
print(len(set_1 & set_2) if len(set_1 & set_2) != 0 else "Таких нет")
