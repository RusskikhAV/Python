"""
        Длины всех слов

Вашему решению будет предоставлена строка sentence слов, разделённых пробелами.

Напишите списочное выражения для генерации списка длин слов.

Примечание
    В решении не должно быть ничего, кроме списочного выражения.
"""
# считываем строку
sentence = input()
# списочным выражением в цикле проходимся по строке разделённой пробелом,
# записываем длину каждого слова
len_word_in_sentence = [len(word) for word in sentence.split(' ')]
print(len_word_in_sentence)
