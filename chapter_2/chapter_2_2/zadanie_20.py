"""
        Зайка — 2

По пути домой родители вновь решили сыграть с детьми в поиск зверушек.

Формат ввода
    Три строки описывающих придорожную местность.

Формат вывода
    Строка в которой есть зайка, а затем её длина.
    Если таких строк несколько, выбрать ту, что меньше всех лексикографически.
"""

# считывание и сохранение введенных с клавиатуры данных
str_1 = input()
str_2 = input()
str_3 = input()


def find_zayka(param1, param2, param3):
    split_string = [param1.split(" "), param2.split(" "), param3.split(" ")]
    res_list = []
    res_str = ""
    for i in range(3):
        for j in range(len(split_string[i])):
            if split_string[i][j] == "зайка":
                if len(res_list) == 0:
                    res_list = split_string[i]
                if res_list != "":
                    if split_string[i] < res_list:
                        res_list = split_string[i]

    for i in range(len(res_list)):
        res_str += res_list[i] + " "

    print(res_str, len(res_str) - 1, sep="")


find_zayka(str_1, str_2, str_3)
