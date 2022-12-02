filename = 'day2.txt'

games = open(filename, 'r').readlines()

def rps(opponent, me):
    if opponent == 'A': # rock
        if me == 'X':  # rock
            return 3, 1
        if me == 'Y':  # paper
            return 6, 2
        if me == 'Z':  # scissors
            return 0, 3
    elif opponent == 'B': # paper
        if me == 'X':  # rock
            return 0, 1
        if me == 'Y':  # paper
            return 3, 2
        if me == 'Z':  # scissors
            return 6, 3
    elif opponent == 'C': # scissors
        if me == 'X':  # rock
            return 6, 1
        if me == 'Y':  # paper
            return 0, 2
        if me == 'Z':  # scissors
            return 3, 3

points = 0
for game in games:
    outcome, shape = rps(game[0], game[2])
    points += (outcome + shape)

print('Total points :', points)

## Part 2

def rps_rigged(opponent, result):
    if opponent == 'A': # rock
        if result == 'X':  # loose (scissors)
            return 0, 3
        if result == 'Y':  # draw (rock)
            return 3, 1
        if result == 'Z':  # win (paper)
            return 6, 2
    if opponent == 'B': # paper
        if result == 'X':  # loose (rock)
            return 0, 1
        if result == 'Y':  # draw (paper)
            return 3, 2
        if result == 'Z':  # win (scissors)
            return 6, 3
    if opponent == 'C': # scissors
        if result == 'X':  # loose (paper)
            return 0, 2
        if result == 'Y':  # draw (scissors)
            return 3, 3
        if result == 'Z':  # win (rock)
            return 6, 1

rigged_points = 0
for game in games:
    outcome, shape = rps_rigged(game[0], game[2])
    rigged_points += (outcome + shape)

print('Total rigged points :', rigged_points)