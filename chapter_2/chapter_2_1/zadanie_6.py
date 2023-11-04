"""
            Чек

Сдачу посчитать, конечно, все могут, но красивый чек напечатать — не так просто.

Формат ввода
      название товара;
      цена товара;
      вес товара;
      количество денег у пользователя.
Формат вывода
      Чек
      <название товара> - <вес>кг - <цена>руб/кг
      Итого: <итоговая стоимость>руб.
      Внесено: <количество денег от пользователя>руб.
      Сдача: <сдача>руб
"""

# последовательное считывание и сохранение введенных с клавиатуры данных
name_of_product = input()
price_for_kg = int(input())
weight_of_product = int(input())
currency = int(input())

# цена за товар, вес * кг
amount = weight_of_product * price_for_kg

# сдача, количество денег у покупателя - цена за товар
change = int(currency - amount)

# не обязательно указывать позиции в фигурных скобках {}, если они идут в параметрах метода .format() последовательно
print("Чек\n{0} - {1}кг - {2}руб/кг\nИтого: {3}руб\nВнесено: {4}руб\nСдача: {5}руб"
      .format(name_of_product, weight_of_product, price_for_kg, amount, currency, change))
