"""
        Магазин

Кроме черешни в магазине продаётся множество других товаров, которые продаются на развес.
Давайте автоматизируем расчёт сдачи и для них!

Формат ввода
    Три натуральных числа:
        цена товара;
        вес товара;
        количество денег у пользователя.
Формат вывода
    Одно целое число — сдача, которую требуется отдать пользователю """

# каст к float, т.к. вес товара, а так же цена может быть не целым числом
price_for_kg = float(input())
tovar_kg = float(input())
currency = float(input())
print(int(currency - tovar_kg * price_for_kg))
