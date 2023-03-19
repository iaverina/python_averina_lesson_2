# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input())
count_heads = 0
count_tails = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count_heads += 1
    else:
        count_tails += 1
if count_tails > count_heads:
    print(count_heads)
else:
    print(count_tails)