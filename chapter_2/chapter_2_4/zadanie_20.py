"""
        Математическая выгода

Математик Виталий Евгеньевич задумался над вопросом выгоды систем счисления. Он решил, что выгодной системой счисления
будет являться та, в которой число имеет наибольшую сумму цифр. Напишите программу, которая по введённому
числу определяет основание системы счисления с максимальной выгодой.

Формат ввода:
    Одно натурально число.

Формат вывода:
    Одно натуральное число из диапазона [2;10] — основание системы счисления с максимальной выгодой.
    Если таких оснований несколько, выбирается наименьшее.
"""

n = int(input())


def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits):
        return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


max_num = 0
system_num = 0
for i in range(2, 11):
    curr_num = 0
    for el in convert_to(n, i):
        curr_num += int(el)
    if curr_num > max_num:
        max_num = curr_num
        system_num = i
print(system_num)
