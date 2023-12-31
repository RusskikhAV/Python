"""
        Список покупок

Поход в магазин часто вызывает проблемы. Если не подготовить список, можно уйти в магазин за хлебом,
а вернуться с десятком пакетов. Напишите программу,
которая собирает пожелания семьи (мамы, папы и дочки) в единый список.

Формат ввода:
    В трёх строках записаны желаемые продукты (через запятую и пробел).

Формат вывода:
    Отсортированный по алфавиту список продуктов с нумерацией.

Примечание
Помните, что итераторы можно применять к другим итераторам.
"""

# имеем 3 строки преобразованные в список
list_mother = input().split(', ')
list_father = input().split(', ')
list_daughter = input().split(', ')
# составляем результирующий список, состоящий из 3х списков
result_list = list_mother + list_father + list_daughter
# методом enumerate добавляем индекс элементу, где начало индексации с 1
for i, value in enumerate(sorted(result_list), start=1):
    print(i, value, sep='. ')
