"""
        Азбука

Знакомые нам воспитанники детского сада наконец-то начали учить буквы.
Воспитатель предложил ребятам назвать слова, которые начинаются с А, Б или В.
Напишите программу, которая проверяет, что первая буква во всех словах — А, Б или В.

Формат ввода:
    Вводится натуральное число N — количество слов, названных детьми.
    В каждой из последующих N строк записано по одному слову строчными буквам.

Формат вывода:
    YES — если все слова начинаются с нужной буквы.
    NO — если хотя бы одно слово начинается не с нужной буквы.
"""

n = int(input())
s = ["а", "б", "в"]
count = 0
for i in range(n):
    words = input()
    if s.count(words[0]) == 0:
        print("NO")
        count += 1
        break

if count == 0:
    print("YES")
