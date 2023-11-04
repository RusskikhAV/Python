"""
        Просто здравствуй, просто как дела

Умение вести диалог — важный навык для воспитанного человека.

Напишите диалоговую программу, которая сначала познакомится с пользователем, а затем поинтересуется его настроением.

Формат ввода
    В первой строке записано имя пользователя.
    Во второй — ответ на вопрос: «хорошо» или «плохо».

Формат вывода
    В первой строке должен быть вопрос «Как Вас зовут?»
    Во второй строке — «Здравствуйте, %username%!»
    В третьей строке — вопрос «Как дела?»
    В четвёртой строке реакция на ответ пользователя:
        - если пользователь ответил «хорошо», следует вывести сообщение «Я за вас рада!»;
        - если пользователь ответил «плохо», следует вывести сообщение «Всё наладится!».
"""

# считывание и сохранение введенных с клавиатуры данных
username = input("Как Вас зовут?\n")
print("Здравствуйте,", username, end="!\n")
dela = input("Как дела?\n")
if "хорошо" in dela.lower():
    print("Я за вас рада!")
else:
    print("Всё наладится!")
