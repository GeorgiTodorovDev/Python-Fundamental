import math

party_size = int(input())
days = int(input())

companion_coins = 50 * days

for each_day in range(1, days + 1):
    if each_day % 10 == 0:
        party_size -= 2
    if each_day % 15 == 0:
        party_size += 5
    companion_coins -= (2 * party_size)
    if each_day % 3 == 0:
        companion_coins -= (3 * party_size)
    if each_day % 5 == 0:
        companion_coins += (20 * party_size)
        if each_day % 3 == 0:
            companion_coins -= (2 * party_size)

companion_coins = math.floor(companion_coins / party_size)
print(f'{party_size} companions received {companion_coins} coins each.')
