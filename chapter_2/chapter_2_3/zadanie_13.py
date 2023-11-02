"""
        Первому игроку приготовиться 2.0

Во многих играх порядок ходов определяется броском кубика или монетки, а в нашей первым ходит тот,
чье имя лексикографически меньше. Определите, кто из игроков будет ходить первым.

Формат ввода:
    В первой строке записано одно натуральное число N — количество игроков.
    В каждой из последующих N строк указано одно имя игрока.

Формат вывода:
    Имя игрока, который будет ходить первым.
"""
number_of_participants = int(input())
i = 0
first_player_name = ""
while i < number_of_participants:
    name = str(input())
    if first_player_name == "":
        first_player_name = name
    elif first_player_name > name:
        first_player_name = name
    i += 1

print(first_player_name)
