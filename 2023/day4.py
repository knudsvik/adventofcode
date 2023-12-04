filename = '2023/input/day4.txt'
cards = open(filename, 'r').readlines()

points = 0

for card in cards:
    winning, playing = card.split(':')[1].strip().split('|')

    win_set = set(map(int, winning.split()))
    play_set = set(map(int, playing.split()))

    wins = win_set.intersection(play_set)
    if len(wins) > 0:
        points += 2**(len(win_set.intersection(play_set))-1)

print(f'Sum points in part 1: {points}')

### PART TWO

scratch_cards = 0

house_of_cards = {}
for card_number in range(1, len(cards)+1):
    house_of_cards[card_number] = 1

card_number = 0
for card in cards:
    card_number += 1
    instances = house_of_cards[card_number]
    scratch_cards += instances

    winning, playing = card.split(':')[1].strip().split('|')

    win_set = set(map(int, winning.split()))
    play_set = set(map(int, playing.split()))

    wins = win_set.intersection(play_set)

    if len(wins) == 0:
        continue

    for instance in range(instances):
        for i in range(1, len(wins)+1):
            house_of_cards[card_number+i] += 1

print(f'Scratch cards in part 2: {scratch_cards}')
