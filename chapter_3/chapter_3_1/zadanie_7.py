"""
        А и Б сидели на трубе

Сложение чисел весьма простая задача.
К сожалению, пользователи не всегда вводят данные так, как нам удобно.

Формат ввода:
    Два целых числа, разделённые пробелом.

Формат вывода:
    Одно целое число — сумма переданных чисел.
"""

# считываю с клавиатуры числа, и разделяю их по пробелу
a_and_b = input().split(" ")
# переменная для хранения суммы двух чисел
sum_of_num = 0
# прохожусь по списку, и нахожу сумму
for i in a_and_b:
    sum_of_num += int(i)
# печатаю результат
print(sum_of_num)
