"""
        НОД 3.0

Местному НИИ в очередной раз нужно находить наибольший общий делитель (НОД) нескольких чисел.
Руководство института вернулось с этой задачей к нам.

Формат ввода:
    В единственной строке записывается последовательность натуральных чисел, разделённых пробелами.

Формат вывода:
    Требуется вывести одно натуральное число — НОД всех данных чисел.

Примечание:
    Самый распространенный способ поиска НОД — Алгоритм Эвклида.
"""


# метод для определения НОД двух чисел
# в нем мы вычитаем от большего меньшее, пока А не будет равно Б
def nod(a, b):
    while a != b:
        if a != 0 and b != 0:
            if a > b:
                a = a - b
            else:
                b = b - a
    return a


# считываем введённую последовательность чисел и разделяем её по пробелу превращая в список num_list
sequence_of_numbers = input()
num_list = sequence_of_numbers.split(" ")
# переменная для НОД всех чисел
nod_list = []
# в двойном цикле прохожу по каждому числу, и нахожу их НОД с каждым не равным ему числом
for i in range(len(num_list)):
    for j in range(i):
        if i == j:
            continue
        nod_list.append(nod(int(num_list[i]), int(num_list[j])))
print(min(nod_list))
