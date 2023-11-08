"""
        Анонс новости

Местная новостная компания заказала сайт. Его неотъемлемая часть — новостная лента.
Чтобы пользователи могли быстрее анализировать статьи, нужно сократить заголовки. Напишите программу,
которая сокращает длинные заголовки до требуемой длины и завершает их многоточием ... при необходимости.

Формат ввода:
    Вводится натуральное число L — необходимая длина заголовка.
    Вводится натуральное число N — количество заголовков, которые требуется сократить.
    В каждой из последующих N строк записано по одному заголовку.

Формат вывода:
    Сокращённые заголовки.

Примечание:
    Многоточие учитывается при подсчёте длины заголовка.
"""

max_length_title = int(input())
number_of_titles = int(input())

for i in range(number_of_titles):
    title = input()
    print(title if len(title) <= max_length_title else title[:max_length_title - 3] + "...")
