"""
        Сборы на прогулку

Воспитатель в детском саду устал тратить время, чтобы построить детей по парам.

Он договорился с детьми, чтобы те делились на две, по возможности равные, группы.

Напишите программу, которая по списку двух шеренг составляет пары детей.

Формат ввода:
    Вводится две строки с именами детей, записанными через запятую и пробел.

Формат вывода:
    Требуется вывести список пар, которые можно составить,
    если последовательно брать из каждой шеренги по одному ребёнку.
    Имена в парах выводить через дефис окружённый пробелами.

Примечание
В одной из групп может быть на одного ребенка больше, чем в другой.
Этот ребёнок при формировании пар не учитывается и идёт в паре с воспитателем.
"""

# принимаем на вход две шеренги детей, превращаем строку в список
group_1 = input().split(' ')
group_2 = input().split(' ')
# используем метод zip обернутый в list получаем список кортежей
pair_child = list(zip(group_1, group_2))
# проходимся по списку, берём первый элемент кортежа это будет ребёнок из 1 шеренги,
# второй элемент кортежа - второй ребёнок, разделяем запись дефисом обрамлённым пробелами
for i in pair_child:
    print(str(i[0]).removesuffix(","), str(i[1]).removesuffix(","), sep=' - ')
