"""
        Цифровая сумма

Иногда требуется манипулировать с цифрами чисел.
Одно из самых простых действий, которое можно совершить — найти сумму цифр числа.
Напишите программу, чтобы выполнить это действие.

Формат ввода:
    Вводится одно натуральное число.

Формат вывода:
    Требуется вывести одно натуральное число — сумму цифр исходного.
"""

number = input()
result = 0
for el in number:
    result += int(el)
print(result)