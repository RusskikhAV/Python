"""
        Кто быстрее?

В главной велогонке года участвует более тысячи гонщиков. Им предстоит пройти трассу длинной 43872м.
Самая сложная и ответственная задача — определение победителя.

Нам известны средние скорости двух фаворитов — Пети и Васи. Помогите выяснить, кто из них пришёл к финишу первым.

Формат ввода
    В первой строке записана средняя скорость Пети.
    Во второй — Васи.

Формат вывода
    Имя победителя гонки.

Примечание
Гарантируется, что победителем стал только один.
"""

# считывание и сохранение введенных с клавиатуры данных
average_speed_petya = int(input())
average_speed_vasya = int(input())


if average_speed_petya > average_speed_vasya:
    print("Петя")
else:
    print("Вася")
