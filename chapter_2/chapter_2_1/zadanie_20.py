"""
        Мухи отдельно, котлеты отдельно

Вернёмся в магазин, хозяин которого уже привык полагаться на всемогущую автоматизацию.

Помогите ему разобраться с одной проблемой. Далее его история:
«Пару дней назад я купил две партии котлет и по случайности высыпал их на один прилавок.
Общий вес котлет составил N килограмм, а ценник — M рублей за килограмм.
Сегодня я обнаружил, что накладные на эти виды котлет потерялись, но я помню, что первый вид котлет стоил
K_1 рублей за килограмм, а второй — K_2.

Помогите мне вспомнить вес каждой партии котлет, чтобы поставить их на учёт.

Формат ввода
    В первой строке записано натуральное число N
    Во второй строке — натуральное число M
    В третьей строке — натуральное число K_1
    В четвёртой строке — натуральное число K_2

Причём доподлинно известно, что второй вид котлет стоит меньше, чем первый.

Формат вывода
    Два натуральных числа, записанных через пробел — вес обеих партий котлет.
"""

# считываем 4 числа N, M, K_1 и K_2
cutlets_weight = int(input())
price = int(input())
cutlets_v_1 = int(input())
cutlets_v_2 = int(input())
k_1 = 1
k_2 = 1
amount = cutlets_weight * price

# в цикле находим вес каждой версии котлет по формуле
# K_1 * 240(цена одного вида котлет) + (32(общий вес) - K_1) * 300(цена другого вида котлет) = 9120(сумма всей партии)
while k_1 * cutlets_v_1 + (cutlets_weight - k_1) * cutlets_v_2 != amount:
    k_1 += 1
    k_2 = cutlets_weight - k_1

print(k_1, k_2)
