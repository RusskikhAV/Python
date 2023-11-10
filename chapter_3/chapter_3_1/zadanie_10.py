"""
        Частотный анализ на минималках

Частотный анализ — подсчёт, какие символы чаще всего встречаются в тексте. Это важнейший инструмент взлома многих
классических шифров — от шифра Цезаря и до шифровальной машины «Энигма». Выполним простой частотный анализ:
выясним, какой символ встречается в тексте чаще всего.

Формат ввода:
    Вводятся строки, пока не будет введена строка «ФИНИШ».

Формат вывода:
    Выводится один символ в нижнем регистре — наиболее часто встречающийся.

Примечания:
    Пробелы в анализе не участвуют.
    Если в результате анализа получено несколько ответов, следует вывести первый по алфавиту.
"""

# создал переменные для сохранения результатов
count, letter, dictionary = 0, "", {}
# в цикле, пока не будет строки "финиш", считываю данные
while (words := input().lower()) != "финиш":
    # прохожусь по каждой букве в словах, и если её еще нет в словаре, добавляю как ключ - буква, а значение
    # количество её повторений (не учитываю пробел как символ), если уже такой символ существует, увеличиваю на 1
    # его повторение
    for i in words:
        if i not in dictionary and i != " ":
            dictionary.update({i: 1})
        elif i != " ":
            dictionary.update({i: dictionary.get(i) + 1})
# собираю все ключи в словаре
keys = dictionary.keys()
# пробегаюсь по словарю с ключами и записываю в переменные максимально встречающийся символ
for i in keys:
    if letter == "":
        letter = i
        count = dictionary.get(i)
        continue
    if dictionary.get(i) > count:
        letter = i
        count = dictionary.get(i)
# вывожу результат
print(letter)
