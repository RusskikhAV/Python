"""
        Суммарная сумма

Найти сумму цифр числа не так сложно, но что, если чисел несколько?
Напишите программу для выполнения этого действия.

Формат ввода:
    В первой строке указано число N Во всех последующих N строках написано по одному числу.

Формат вывода:
    Требуется вывести общую сумму цифр всех введённых чисел (кроме N).
"""

n = int(input())
res = 0
i = 0
while i < n:
    number = input()
    for el in number:
        res += int(el)
    i += 1
print(res)
