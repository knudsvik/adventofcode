filename = '2023/input/day2.txt'
sack = open(filename, 'r').readlines()

red_max = 12
green_max = 13
blue_max = 14

game_id  = 0
sum = 0

for game in sack:
    game_id += 1
    game_possible = True
    #print(f"game: {game}")
    revealed = game.split(':', 1)[1].strip()

    for subset in revealed.split(';'):
        # print(f"  subset: {subset}")
        red, green, blue = 0, 0, 0
        
        for colours in subset.split(','):
            number, colour = colours.split()
            number = int(number)
            
            if colour == "red" and number > red_max: game_possible = False
            if colour == "green" and number > green_max: game_possible = False
            if colour == "blue" and number > blue_max: game_possible = False

    if game_possible:
        sum += game_id

print(f"The sum of part 1 is {sum}")  # 2061
        
### PART TWO

game_id  = 0
sum = 0

for game in sack:
    game_id += 1
    #print(f"game: {game}")
    revealed = game.split(':', 1)[1].strip()
    
    red_min, green_min, blue_min = 0, 0, 0
    
    for subset in revealed.split(';'):
        # print(f"  subset: {subset}")
        red, green, blue = 0, 0, 0
        
        for colours in subset.split(','):
            number, colour = colours.split()
            number = int(number)
            
            if colour == "red" and number > red_min: red_min = number
            if colour == "green" and number > green_min: green_min = number
            if colour == "blue" and number > blue_min: blue_min = number

    power = red_min * green_min * blue_min
    sum += power
    print(f"Fewest in game {game_id}: {power}")

print(f"The sum of part 2 is {sum}") 