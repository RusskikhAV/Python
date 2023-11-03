"""
        Зайка — 5

В долгой дороге дети вновь заскучали, и родителям приходится их развлекать поиском зверушек за окном.
Давайте вместе с ними найдём заек.

Формат ввода:
    В первой строке указано натуральное число N — количество выделенных придорожных местностей.
    В последующих строках записаны слова характеризующие выделенную местность.
    Информация о каждой местности завершается словом «ВСЁ».

Формат вывода:
    Количество местностей, в которых есть зайка.
"""
n = int(input())
i = 0
count = 0
current_string = []
while i < n:
    while (input_str := input()) != "ВСЁ":
        current_string.append(input_str)
    if current_string.count("зайка") > 0:
        count += 1
    print(current_string)
    current_string = []
    i += 1
print(count)
