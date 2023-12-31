"""
        Дайте чего-нибудь новенького!

Главный повар детского сада хочет приготовить в праздничный день блюда, которые ни разу не готовил на этой неделе.
В его распоряжении есть список блюд:
    - которые можно приготовить в столовой сегодня;
    - которые были приготовлены в каждый из дней недели.

Формат ввода:
    Число блюд (N), которые можно приготовить в столовой.
    N строк с названиями блюд. Число дней (M), о которых имеется информация.
    M блоков строк для каждого из списков.
    В первой строке каждого блока записано число блюд в заданный день, затем перечисляются эти блюда.

Формат вывода:
    Список блюд, которые ещё не готовились на этой неделе в алфавитном порядке.
    Если все возможные блюда уже были приготовлены, следует вывести «Готовить нечего».
"""

# создаём список блюд которые можно приготовить
delicious = []
# считываем количество блюд, в цикле заполняем список
num_delicious = int(input())
for i in range(num_delicious):
    delicious.insert(i, input())
# узнаём количество дней с информацией о приготовленных блюдах - num_information,
# далее узнаем сколько блюд было приготовлено в текущий день - num_current_delicious,
# смотрим на конкретное current_delicious блюдо, если такое есть в списке блюд которые можно приготовить,
# удаляем из списка, в итоге останется только то, что еще не готовили, иначе "Готовить нечего"
num_information = int(input())
for i in range(num_information):
    num_current_delicious = int(input())
    for k in range(num_current_delicious):
        current_delicious = input()
        if current_delicious in delicious:
            delicious.remove(current_delicious)

if len(delicious) > 0:
    for i in sorted(delicious):
        print(i)
else:
    print("Готовить нечего")
