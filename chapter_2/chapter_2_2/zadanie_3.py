"""
        Кто быстрее на этот раз?

Вновь велогонщики собрались узнать, кто из них быстрее.
Им предстоит пройти трассу длиной 43872м, и нам нужно вновь определить победителя.

На этот раз нам известны средние скорости трёх фаворитов — Пети, Васи и Толи. Кто из них пришёл к финишу первым?

Формат ввода
    В первой строке записана средняя скорость Пети.
    Во второй — Васи.
    В третьей — Толи.

Формат вывода
    Имя победителя гонки.

Примечание
Гарантируется, что победителем стал только один.
"""

# считывание и сохранение введенных с клавиатуры данных
n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

name_petya = "Петя"
name_vasya = "Вася"
name_tolya = "Толя"

# проверяю кто первый с помощью тернарного оператора, запись получилась короче, чем if-elif-else
print(name_petya if n_2 < n_1 > n_3 else name_vasya if n_1 < n_2 > n_3 else name_tolya)

# if n_2 < n_1 > n_3:
#     print("Петя")
# elif n_1 < n_2 > n_3:
#     print("Вася")
# else:
#     print("Толя")
