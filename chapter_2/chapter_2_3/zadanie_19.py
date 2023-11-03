"""
        Игра в «Угадайку»

Давайте сымитируем игру «Угадайка» между двумя людьми. Для этого нужно написать программу,
которая отгадывает загаданное целое число от 1 до 1000 включительно.
Пользователь (или тестирующая система) загадывает число и не сообщает его вашей программе.
Угадать число нужно не более, чем за 10 попыток.

На каждую попытку пользователь отвечает одной из фраз:
    Больше;
    Меньше;
    Угадал!
Данная задача проверяется интерактивно. Другими словами, пока вы не выведите своё число, система не предоставит вам данных.
"""
# import random
# count = 1
# # random_number = random.randint(1, 1000)
# string = input()
# random_number = int(input())
# while (input_number := int(input())) != random_number:
#     if count == 10:
#         break
#     if int(input_number) < int(random_number):
#         print("Больше")
#         count += 1
#     elif int(input_number) > int(random_number):
#         print("Меньше")
#         count += 1
#
# if input_number == random_number:
#     print("Угадал!")

list_num = []
for i in range(1, 1001):
    list_num.append(i)

count = list_num[int(len(list_num) / 2)]
# random_number = random.randint(1, 1000)
print(count)
while (input_number := input()) != "Угадал!":
    # print(count)
    if input_number == "Больше":
        list_num = list_num[list_num.index(count): len(list_num)]
        count = list_num[int(len(list_num) / 2)]
        print(count)
    elif input_number == "Меньше":
        list_num = list_num[0: list_num.index(count)]
        count = list_num[int(len(list_num) / 2)]
        print(count)

