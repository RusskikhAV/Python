"""
        Внимание! Акция!

В продуктовом магазине объявили акцию: «На все товары с ценой не менее 500 тугриков предоставляется скидка 10%».
Нас попросили разработать программное обеспечение кассового автомата,
которое будет считать итоговую сумму покупки с учётом скидки.

Формат ввода:
    Вводится некоторое количество рациональных чисел — стоимость товаров.
    Список завершается значением 0.

Формат вывода:
    Требуется вывести сумму всех товаров с учётом объявленной акции.
"""

amount_with_discount = 0.0
discount = 0.9
while (amount_without_discount := float(input())) != 0.0:
    if amount_without_discount >= 500.0:
        amount_with_discount += amount_without_discount * discount
    else:
        amount_with_discount += amount_without_discount
print(amount_with_discount)
