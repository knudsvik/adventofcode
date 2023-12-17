filename = '2023/input/day16.txt'
lines = open(filename, 'r').readlines()

# Coordinate system:
cs = [list(line.strip()) for line in lines]
energized = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]


def step(x, y, dir):
    symbol = cs[y][x]        
    if symbol == '.':
        if dir == 'W':
            x = x - 1
        elif dir == 'E':
            x = x + 1
        elif dir == 'N':
            y = y - 1
        elif dir == 'S':
            y = y + 1
    elif symbol == '\\':
        if dir == 'W':
            y = y - 1
            dir = 'N'
        elif dir == 'E':
            y = y + 1
            dir = 'S'
        elif dir == 'N':
            x = x - 1
            dir = 'W'
        elif dir == 'S':
            x = x + 1
            dir = 'E'
    elif symbol == '/':
        if dir == 'W':
            y = y + 1
            dir = 'S'
        elif dir == 'E':
            y = y - 1
            dir = 'N'
        elif dir == 'N':
            x = x + 1
            dir = 'E'
        elif dir == 'S':
            x = x - 1
            dir = 'W'
    elif symbol == '|':
        if dir == 'W' or dir == 'E':
            if not (x, y - 1, "N") in beam_starts:
                beam_starts.append((x, y - 1, "N"))
            y = y + 1
            dir = 'S'
        elif dir == 'N':
            y = y - 1
        elif dir == 'S':
            y = y + 1
    elif symbol == '-':
        if dir == 'W':
            x = x - 1
        elif dir == 'E':
            x = x + 1
        elif dir == 'N' or dir == 'S':
            if not (x + 1, y, "E") in beam_starts:
                beam_starts.append((x + 1, y, "E"))
            x = x - 1
            dir = 'W'
    return x, y, dir

# x, y, direction
beam_starts = [(0, 0, 'E')]

for beam in beam_starts:
    x = beam[0] 
    y = beam[1]  
    dir = beam[2]
    steps = 0  # To hinder loops

    if not (0 <= x < len(lines[0])) or not (0 <= y < len(lines)):
        continue

    energized[y][x] = True
    
    while not (x == len(lines[0]) - 1 and y == len(lines) - 1):
        x, y, dir = step(x, y, dir)
        if not (0 <= x < len(cs[0])) or not (0 <= y < len(lines)):
            break
        energized[y][x] = True
        steps += 1
        if steps > 1000: # Encountered a loop
            break
    
    #print(f"Beam {beam} has come to an end with {steps} steps")


sum = sum(cell for row in energized for cell in row)
print(sum)