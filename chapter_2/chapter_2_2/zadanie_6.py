"""
        Сила прокрастинации

Вася любит полениться. Особенно ему нравится, когда в году появляется такой лишний денёк, которого обычно не бывает.
Напишите программу, которая поможет Васе определить, удастся ли ему побездельничать в определённом году или нет.

Формат ввода
    Одно число — год.

Формат вывода
    Одно слово «YES» (удастся) или «NO» (не удастся).
"""

year = int(input())
if year % 4 == 0:
    if year % 400 != 0 and year % 100 == 0:
        print("NO")
    else:
        print("YES")
else:
    print("NO")
