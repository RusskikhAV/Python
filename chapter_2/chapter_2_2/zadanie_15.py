"""
        Властелин Чисел: Возвращение Цезаря

До победы над злом остался один шаг — разрушить логово Зерона.
Для этого нужно создать трёхзначное магическое число, которое будет сильнее двух двухзначных защитных чисел Зерона.

Самый простой способ создать сильное число:
    первой взять максимальную цифру из всех защитных чисел;
    последней — минимальную;
    в середину поставить сумму оставшихся без учёта переноса разряда.
Помогите одолеть зло.

Формат ввода
    В двух строках записаны защитные числа Зерона.

Формат вывода
    Одно трёхзначное число, которое приведёт к победе.
"""

number_1 = list(input())
number_2 = list(input())

min_num_1 = min(number_1)
max_num_1 = max(number_1)

min_num_2 = min(number_2)
max_num_2 = max(number_2)

result = ""

if int(max_num_1) > int(max_num_2):
    result += str(max_num_1)
    number_1.remove(max_num_1)
else:
    result += str(max_num_2)
    number_2.remove(max_num_2)

if int(min_num_1) < int(min_num_2):
    result += str(min_num_1)
    number_1.remove(min_num_1)
else:
    result += str(min_num_2)
    number_2.remove(min_num_2)

summa = 0
if len(number_1) > 0 and len(number_2) > 0:
    summa = (int(number_1[0]) + int(number_2[0])) % 10
elif len(number_1) >= 1:
    summa = (int(number_1[0]) + int(number_1[1])) % 10
else:
    summa = (int(number_2[0]) + int(number_2[1])) % 10

res = list(result)
res.insert(1, summa)

result = str(res[0]) + str(res[1]) + str(res[2])
print(result)