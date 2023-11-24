"""
        Двоичная статистика!

У программистов особые отношения с двоичной системой счисления.
Продолжим тренировки в статистической обработке данных и проанализируем данные числа.
Напишите программу, которая для переданных чисел вычисляет:
    - количество разрядов;
    - количество единиц;
    - количество нулей.

Формат ввода:
    Вводится последовательность чисел, записанных через пробел.

Формат вывода:
    Вывести список словарей с требуемой статистикой.

Примечание:
    Вывод в примерах отформатирован только для визуальной наглядности.
    Все пробельные символы при проверке игнорируются.
    Порядок словарей обязан совпадать с порядком переданных чисел.
    Порядок ключей в словаре не имеет значения.
"""

# считываем список чисел и разделяем их по пробелу
input_numbers = input().split(" ")
# создаём лист, в котором будем хранить словари в необходимом формате
list_of_dict_num = []
# Проходим по всем числам, переводим в двоичную систему удаляя префикс.
# Во внутреннем цикле подсчитываем количество нулей и единиц.
# Создаем словарь, с необходимыми значениями, где:
# 'digits' количество разрядов, равно длине строки,
# 'units' количество единиц,
# 'zeros' количество нулей.
# В конец листа добавляем созданный словарь
for i in input_numbers:
    s = bin(int(i)).removeprefix("0b")
    units = 0
    zeros = 0
    for j in s:
        if j == '1':
            units += 1
        elif j == '0':
            zeros += 1
    dict_current_num = {'digits': len(s), 'units': units, 'zeros': zeros}
    list_of_dict_num.append(dict_current_num)
# печатаем результат
print(list_of_dict_num)