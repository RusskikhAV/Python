"""
        Яблоки

У Пети было 7 яблок, а у Васи 6. Затем Петя отдал 3 яблока Васе, а у Толи взял 2 яблока.
Вася попросил у Толи 5 яблок, но он отдал Гене 2. Затем Дима дал Пете N яблок, а Васе M.

Так у кого в итоге яблок больше — у Пети или Васи?

Формат ввода
    В первой строке записано натуральное число N.
    Во второй — M.

Формат вывода
    Имя ребёнка, у которого больше яблок.
"""

petya = 6
vasya = 9

dima_for_petya = int(input())
dima_for_vasya = int(input())

petya += dima_for_petya
vasya += dima_for_vasya

name_petya = "Петя"
name_vasya = "Вася"

print(name_petya if petya > vasya else name_vasya)

# if petya > vasya:
#     print("Петя")
# else:
#     print("Вася")
