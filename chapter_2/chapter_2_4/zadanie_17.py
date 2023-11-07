"""
        А роза упала на лапу Азора 3.0

Вернёмся к палиндромам. Напишите программу, которая определяет количество палиндромов в переданном списке.

Формат ввода:
    В первой строке записано число N Во всех последующих N строках указано по одному числу.

Формат вывода:
    Требуется вывести общее количество палиндромов среди введённых чисел (кроме числа N).
"""


def is_palindrom(palindrom):
    # проверяю, из четного количества цифр состоит палиндром
    if len(palindrom) % 2 == 0:
        # далее беру его вторую половину
        rev_pal = palindrom[int(len(palindrom) / 2):int(len(palindrom))]
        # и сверяю её в перевернутом виде с первой частью
        if str(rev_pal[::-1]) == str(palindrom[0:int(len(palindrom) / 2)]):
            return True
        else:
            return False
    else:
        rev_pal = palindrom[int((len(palindrom) / 2) + 1):int(len(palindrom))]
        if str(rev_pal[::-1]) == str(palindrom[0:int(len(palindrom) / 2)]):
            return True
        else:
            return False


# считывание и сохранение введенных с клавиатуры данных
n = int(input())
# переменная для подсчета количества палиндромов, если метод is_palindrom вернул истина, увеличиваю на 1
count = 0
for i in range(n):
    if is_palindrom(input()):
        count += 1

print(count)
