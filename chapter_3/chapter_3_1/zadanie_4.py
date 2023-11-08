"""
        Очистка данных

Местный провайдер собирает большое количество логов, однако зачастую файлы с отчётами приходят в негодность.
Самые частые проблемы — ошибки вида ## и @@@.
Напишите программу, которая избавляется от:
    Двух символов # в начале информационных сообщений;
    Строк, заканчивающихся тремя символами @.

Формат ввода:
    Вводятся строки отчёта. Признаком завершения ввода считается пустая строка.

Формат вывода
    Очищенные данные
"""

fragment_1 = "##"
fragment_2 = "@@@"

while (n := input()) != "":
    if n.endswith(fragment_2):
        continue
    s = n.removeprefix(fragment_1)
    print(s)
