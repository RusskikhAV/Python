"""
        А роза упала на лапу Азора

Существуют такое интересное понятие как палиндром — число, слово, предложение и так далее,
которое и слева-направо, и справа-налево читается одинаково.

Напишите программу, которая проверяет, является ли число палиндромом.

Формат ввода
    Одно четырёхзначное число

Формат вывода
    YES если число является палиндромом, иначе — NO.
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
