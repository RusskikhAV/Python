"""
        Простая задача 2.0

В банке решили переписать программу для шифрования данных и попросили, чтобы вы взяли на себя часть данной задачи.
Напишите программу для разложения числа на простые множители. Только внимательно,
ведь работать придётся вновь с простыми числами.

Формат ввода:
    Вводится одно натуральное число.

Формат вывода:
    Требуется составить математическое выражение — произведение простых неубывающих чисел,
    которое в результате даёт исходное.
"""


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def simple_method(n):
    a = 0
    b = 0
    for i in range(2, n):
        if n % i == 0:
            a = i
            b = int(n / i)
            break
    return a, b


num = int(input())

res_list = list(simple_method(num))
while not is_prime(res_list[-1]):
    sn = simple_method(res_list[-1])
    res_list.pop()
    res_list.append(sn[0])
    res_list.append(sn[1])

result_string = ""
for el in res_list:
    if result_string == "":
        result_string += str(el)
    else:
        result_string += " * " + str(el)
print(result_string)
