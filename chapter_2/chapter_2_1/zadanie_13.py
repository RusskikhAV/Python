"""
        Дед Мороз и конфеты

Настало самое главное событие в детском саду — новогодний утренник.
Хорошо замаскированная робоняня в роли Деда Мороза решила раздать детям конфеты так,
чтобы каждому досталось поровну.
Напишите для робоняни алгоритм, который поможет распределить конфеты.

Формат ввода
    В первой строке указано количество детей на утреннике.
    Во второй строке — количество конфет в конфетном отсеке робоняни.

Формат вывода
    Сначала выведите количество конфет, которое выдано каждому ребенку,
    а затем количество конфет, что осталось в конфетном отсеке.
"""

# считывание и сохранение введенных с клавиатуры данных
quantity_of_children = int(input())
quantity_of_candy = int(input())

# максимум конфет которые можно выдать одному ребенку
in_one_hands = int(quantity_of_candy / quantity_of_children)

# остаток конфет в конфетном отсеке
residual = quantity_of_candy - in_one_hands * quantity_of_children

# вывод в консоль, где sep="\n" означает что разделятся строки будут переносом строки
print(in_one_hands, residual, sep="\n")
