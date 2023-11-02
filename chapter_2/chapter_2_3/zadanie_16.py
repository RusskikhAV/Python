"""
        А роза упала на лапу Азора 2.0

Вспомним о палиндромах, которые в обоих направлениях читаются одинаково.
Напишите программу, которая проверяет, является ли число палиндромом.

Формат ввода:
    Одно натуральное число.

Формат вывода:
    YES — если число является палиндромом, иначе — NO.
"""

palindrom = input()

# проверяю, из четного количества цифр состоит палиндром
if len(palindrom) % 2 == 0:

    # далее беру его вторую половину
    rev_pal = palindrom[int(len(palindrom) / 2):int(len(palindrom))]

    # и сверяю её в перевернутом виде с первой частью
    if str(rev_pal[::-1]) == str(palindrom[0:int(len(palindrom) / 2)]):
        print("YES")
    else:
        print("NO")
else:
    rev_pal = palindrom[int((len(palindrom) / 2) + 1):int(len(palindrom))]
    if str(rev_pal[::-1]) == str(palindrom[0:int(len(palindrom) / 2)]):
        print("YES")
    else:
        print("NO")
