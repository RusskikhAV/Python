"""
        Интересное сложение

Один малыш из детского сада услышал от старшей сестры о некоем действии с числами — сложении.
И как это часто бывает — он не до конца разобрался, как работает сложение.
Например, не совсем понял, как произвести перенос разряда.
Теперь он хочет научить сложению остальных ребят и просит написать программу,
которая поможет ему в качестве наглядного материала.

Формат ввода
    В первой и второй строках записаны натуральные числа меньше 1000.

Формат вывода
    Одно число — результат сложения введённых чисел без учёта переносов.
"""

number_1 = input().zfill(3)
number_2 = input().zfill(3)
print((int(number_1[0]) + int(number_2[0])) % 10,
      int(int(number_1[1]) + int(number_2[1])) % 10,
      int(int(number_1[2]) + int(number_2[2])) % 10,
      sep="")