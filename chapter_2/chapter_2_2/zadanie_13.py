"""
        Властелин Чисел: Братство общей цифры

Во времена магии и драконов существовало мнение, что числа обладают великой силой, способной изменить мир.
Всё началось с написания великих чисел. Три числа были переданы эльфам. Семь — отданы повелителям гномов.
А девять... были переданы человеческому роду.
Но все они оказались обмануты, потому что существовало ещё одно число.
В стране Нумия на бумаге из тёмного папируса властелин Зерон тайно написал Единую Цифру,
 подчиняющую себе все великие числа.

Давайте выясним, что это за цифра.

Формат ввода
    В первой строке записано двузначное число одного из эльфов.
    Во второй строке — Гномов.
    В третьей — Людей.

Формат вывода
    Одна цифра — общая у всех трёх чисел в одинаковой позиции
"""

# считывание и сохранение введенных с клавиатуры данных
elf = input()
dwarf = input()
human = input()

if elf[0] == dwarf[0] == human[0]:
    print(elf[0])
else:
    print(elf[1])
