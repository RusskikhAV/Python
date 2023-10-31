"""
        В ожидании доставки

Сегодня в N часов M минут хозяин магазина заказал доставку нового товара.
Оператор сказал, что продукты доставят через T минут.
Сколько будет времени на электронных часах, когда привезут долгожданные продукты?

Формат ввода
    В первой строке записано натуральное число N (0≤N<24).
    Во второй строке записано натуральное число M (0≤M<60).
    В третьей строке записано натуральное число T (30≤T<10^9).

Формат вывода
    Одна строка, представляющая циферблат электронных часов.
"""

number_n = int(input())
number_m = int(input())
number_t = int(input())

# расчет количества часов и минут времени Т доставки продуктов
hours = int(number_t / 60)
minutes = number_t % 60

final_delivery_hours = number_n + hours

# вычитаем сутки
while final_delivery_hours > 24:
    final_delivery_hours -= 24

final_delivery_minutes = number_m + minutes

# если в итоге осталось > 60 минут, добавляем +1 к часу, вычитаем 60 минут
while final_delivery_minutes > 60:
    final_delivery_minutes -= 60
    final_delivery_hours += 1

# переводим 24 часа в 00
if str(final_delivery_hours) == "24":
    final_delivery_hours = "00"
print(str(final_delivery_hours).zfill(2), ":", str(final_delivery_minutes).zfill(2), sep="")
