"""
        Зайка — 10

Поможем детям разобраться, что именно они увидели рядом с зайками.

Формат ввода:
    В каждой строке записано описание придорожной местности.
    Конец ввода обозначается пустой строкой.

Формат вывода:
    Определите список увиденного рядом с зайками без повторений.
    Порядок вывода не имеет значения.

Примечание:
    Считается, что объект находится рядом, если он записан справа или слева от требуемого.
"""

# создаём словарь, в котором как ключ будем хранить необходимые нам данные, значение в данном случае не важно
dict_area_object = {}
# слово по которому ищем объекты по близости
search_word = "зайка"
# считываем строки с клавиатуры, пока не будет пустой строки
while (description_area := input()) != "":
    # разделяем строку по пробелам образуя лист
    split_description_area = description_area.split(" ")
    # проверяем если есть искомое слово в переданной строке, запускаем цикл
    if search_word in split_description_area:
        # в котором проходимся по каждому элементу проверяя, равенство с search_word
        for i in range(len(split_description_area)):
            if split_description_area[i] == search_word:
                # если search_word находится на последней позиции в списке, то берём только предыдущий элемент
                if split_description_area[i] == search_word and i == len(split_description_area) - 1:
                    if split_description_area[len(split_description_area) - 2] == split_description_area:
                        continue
                    dict_area_object[split_description_area[len(split_description_area) - 2]] = 1
                # если search_word первый в списке, берем только следующий элемент
                elif split_description_area[i] == search_word and i == 0:
                    if split_description_area[1] == search_word:
                        continue
                    dict_area_object[split_description_area[1]] = 1
                # иначе, берем два элемента, слева и справа от search_word
                else:
                    if split_description_area[i - 1] == search_word or split_description_area[i - 1] == search_word:
                        continue
                    dict_area_object[split_description_area[i - 1]] = 1
                    dict_area_object[split_description_area[i + 1]] = 1
# так как ключи уникальны, это и будет наш список увиденного без повторений
for i in dict_area_object:
    print(i)
