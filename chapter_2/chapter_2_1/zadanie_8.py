"""
        Наказание

Наше развлечение не осталось незамеченным...
И наказание нам выбрали соответствующее.

Формат ввода
    В первой строке записано одно натуральное число N
    Во второй строке записана часть наказания.

Формат вывода
    N строк вида: Я больше никогда не буду писать "<часть наказания>"!
"""

# считывание и сохранение введенных с клавиатуры данных
number = int(input())
string = input()

# f - строкой в {} скобках размещаем string, после чего умножаем получившуюся строку на number
print(f"Я больше никогда не буду писать \"{string}\"!\n" * number)