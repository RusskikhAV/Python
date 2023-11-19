"""
        Польский калькулятор — 2

Потренируемся в ОПН дальше. Операции, которые выполняются с одним значением, называются унарными, с двумя — бинарными,
 с тремя — тернарными. Давайте улучшим наш калькулятор, добавив поддержку следующих операций:
    - бинарные:
        + (сложение)
        - (вычитание)
        * (умножение)
        / (деление нацело; для отрицательных чисел работает по тем же правилам, что и в Python);
    - унарные:
        ~ (унарный минус — меняет знак),
        ! (факториал),
        # (клонирование — вернуть в стек значение дважды);
    - тернарные:
        @ (возвращает в стек те же три значения, но в ином порядке: второе, третье, первое).

Формат ввода:
Вводится одна строка, содержащая разделённые пробелами целые числа и знаки операций.
Вместе они составляют корректное выражение в обратной польской нотации, не содержащее деления на ноль
и взятия факториала от отрицательного числа.

Формат вывода:
Выводится одно целое число — результат вычисления выражения.
"""
import math


# в методе, при встрече первого знака, берем два предыдущих числа и совершаем операцию над ними, помещаем результат
# в ячейку i, удаляем числа над которыми совершена искомая операция
def transcript_opn(list_opn):
    new_list_opn = []
    for i, el in enumerate(list_opn):
        # бинарная операция - произведение
        if el == "*":
            # присваиваю new_list_opn копию листа list_opn
            new_list_opn = list_opn.copy()
            # удаляю знак операции
            new_list_opn.pop(i)
            # на место удаленного знака помещаю результат операции
            new_list_opn.insert(i, int(list_opn[i - 2]) * int(list_opn[i - 1]))
            # удаляю множители произведения
            new_list_opn.pop(i - 1)
            new_list_opn.pop(i - 2)
            # выхожу из цикла
            break
        # бинарная операция - сложение
        elif el == "+":
            new_list_opn = list_opn.copy()
            new_list_opn.pop(i)
            new_list_opn.insert(i, int(list_opn[i - 2]) + int(list_opn[i - 1]))
            new_list_opn.pop(i - 1)
            new_list_opn.pop(i - 2)
            break
        # бинарная операция - вычитание
        elif el == "-":
            new_list_opn = list_opn.copy()
            new_list_opn.pop(i)
            new_list_opn.insert(i, int(list_opn[i - 2]) - int(list_opn[i - 1]))
            new_list_opn.pop(i - 1)
            new_list_opn.pop(i - 2)
            break
        # бинарная операция - деление
        elif el == "/":
            new_list_opn = list_opn.copy()
            new_list_opn.pop(i)
            new_list_opn.insert(i, int(int(list_opn[i - 2]) // int(list_opn[i - 1])))
            new_list_opn.pop(i - 1)
            new_list_opn.pop(i - 2)
            break
        # унарная операция - клонирование
        elif el == "#":
            new_list_opn = list_opn.copy()
            new_list_opn.pop(i)
            new_list_opn.insert(i, list_opn[i - 1])
            break
        # унарная операция - факториал
        elif el == "!":
            new_list_opn = list_opn.copy()
            new_list_opn.pop(i)
            new_list_opn.insert(i, math.factorial(int(list_opn[i - 1])))
            new_list_opn.pop(i - 1)
            break
        # унарная операция - смена знака
        elif el == "~":
            new_list_opn = list_opn.copy()
            new_list_opn.pop(i)
            new_list_opn.insert(i, (int(list_opn[i - 1]) * -1))
            new_list_opn.pop(i - 1)
            break
        # тернарная операция - смена порядка
        elif el == "@":
            new_list_opn = list_opn.copy()
            new_list_opn.pop(i)
            new_list_opn.insert(i, (list_opn[i - 3]))
            new_list_opn.insert(i, (list_opn[i - 1]))
            new_list_opn.insert(i, (list_opn[i - 2]))
            new_list_opn.pop(i - 1)
            new_list_opn.pop(i - 2)
            new_list_opn.pop(i - 3)
            break
    return new_list_opn


# получаю строку в записи ОПН
opn = input()
# разделяю её по пробелу
list_opn = opn.split(" ")
# в цикле пока у меня не останется один элемент, вызываю метод
while len(list_opn) > 1:
    list_opn = transcript_opn(list_opn)
# печатаю первый элемент листа, это будет результат работы программы
print(list_opn[0])
