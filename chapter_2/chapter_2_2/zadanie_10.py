"""
        Лучшая защита — шифрование

Коля испугался, что Аня подсмотрит все его пароли в блокноте, и решил их зашифровать.
Для этого он берёт изначальный пароль — трёхзначное число — и по нему строит новое число по следующим правилам:
    - находится сумма цифр, стоящих в двух младших разрядах (десятки и единицы);
    - находится сумма цифр, стоящих в двух старших разрядах (сотни и десятки)
    - Эти две суммы, записанные друг за другом, в порядке не возрастания, формируют новое число.

Помогите реализовать алгоритм шифрования.

Формат ввода
    Одно трёхзначное число

Формат вывода
    Результат шифрования
"""

# считывание и сохранение введенных с клавиатуры данных
password = input()

# находим сумму старших и младших отрядов
high_order = int(password[0]) + int(password[1])
inferior_order = int(password[1]) + int(password[2])

# для записи в порядке возрастания, используем тернарный оператор
print(high_order if high_order > inferior_order else inferior_order,
      high_order if high_order < inferior_order else inferior_order,
      sep="")
