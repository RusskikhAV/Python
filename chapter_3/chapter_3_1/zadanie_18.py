"""
        RLE

RLE означает “run-length encoding”. Это способ сокращённой записи последовательности чего угодно
(в случае этой задачи — цифр). При нём для подряд идущей группы одинаковых цифр (run) записываются сама эта цифра
и длина этой группы (run length). Таким образом, 99999 превратится в 9 5 («девять пять раз») и так далее. RLE широко
используется в самых разных областях. Напишите программу, которая кодирует строку цифр в RLE.

Формат ввода:
    Строка цифр длиной не меньше 1.

Формат вывода:
    Пары:
    сама цифра и количество повторений цифры подряд во введённой строке, как описано в условии и показано в примере.
"""

# считываю строку с клавиатуры
before_rle = input()
# будем вести подсчет символов в цикле с помощью переменной count
count = 1
# переменная для хранения текущего символа
current_symbol = ""
# в цикле прохожу по строке, беру первый символ, если текущий символ последовательности пуст, записываю его туда,
# тут же и каждый раз проверяю, является ли текущий символ последним, если да печатаю символ и количество его повторений
# если текущий символ равен итерационному, увеличиваю счетчик на единицу,
# если не равен, печатаю символ и количество его повторений, обновляю счетчик и текущий символ
for i in range(len(before_rle)):
    if current_symbol == "":
        current_symbol = before_rle[i]
        if i == (len(before_rle) - 1):
            print(current_symbol, count)
    elif current_symbol == before_rle[i]:
        count += 1
        if i == (len(before_rle) - 1):
            print(current_symbol, count)
    elif current_symbol != before_rle[i]:
        print(current_symbol, count)
        count = 1
        current_symbol = before_rle[i]
        # print(sto[i], len(sto) - 1, sto[i], sep="_")
        if i == (len(before_rle) - 1):
            print(current_symbol, count)