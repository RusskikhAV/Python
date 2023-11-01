"""
        Зайка — 3

В задачнике ко второй лекции мы помогали детям искать зайца.
На этот раз мы будем искать и считать сразу нескольких зайчат.

Формат ввода:
    Вводятся строки, описывающие придорожную местность.
    В конце поездки вводится «Приехали!»

Формат вывода:
    Количество строк, в которых есть зайка.
"""

count = 0
while (description_of_the_area := input().lower()) != "приехали!":
    description_of_the_area_list = description_of_the_area.split(" ")
    for el in description_of_the_area_list:
        if el.lower() == "зайка":
            count += 1
print(count)
