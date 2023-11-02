"""
        Зайка - 4

Давайте вновь поиграем с детьми и поможем им найти заек.

Формат ввода:
    В первой строке записано натуральное число N — количество выделенных придорожных местностей.
    В каждой из N последующих строках — описание придорожной местности.

Формат вывода
    Количество строк, в которых есть зайка.
"""

num = int(input())
count = 0
i = 0
while i < num:
    description_of_the_area = input().lower()
    description_of_the_area_list = description_of_the_area.split(" ")
    for el in description_of_the_area_list:
        if el.lower() == "зайка":
            count += 1
    i += 1
print(count)
