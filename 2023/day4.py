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

print(f'Sum part 1: {points}')