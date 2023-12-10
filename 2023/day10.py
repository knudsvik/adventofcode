filename = '2023/input/day10_samples.txt'
filename = '2023/input/day10.txt'
lines = open(filename, 'r').readlines()

# Coordinate system:
cs = [list(line.strip()) for line in lines]

# Find S:
for Sy, line in enumerate(lines):
    if 'S' in line:
        Sx = line.find('S')
        print(f"{cs[Sy][Sx]} is in line: {Sy}, position: {Sx}")
        break

x, y = Sx, Sy

W = cs[y][x - 1]
S = cs[y + 1][x]
if W == '-':
    x = x - 1
    dir = 'W'
elif W == 'F':
    x = x - 1
    y = y + 1
    dir = 'S'
elif W == 'L':
    x = x - 1
    y = y - 1
    dir = 'N'
elif S == '|':
    y = y + 1
    dir = 'S'
elif S == 'L':
    y = y + 1
    x = x + 1
    dir = 'E'
elif S == 'J':
    y = y + 1
    x = x - 1
    dir = 'W'

def step(x, y, dir, symbol):
    if symbol == '-':
        if dir == 'W':
            x = x - 1
        elif dir == 'E':
            x = x + 1
        else:
            raise ValueError("Something is out of order")
    elif symbol == 'F':
        if dir == 'W':
            y = y + 1
            dir = "S"
        elif dir == 'N':
            x = x + 1
            dir = "E"
        else:
            raise ValueError("Something is out of order")
    elif symbol == 'L':
        if dir == 'W':
            y = y - 1
            dir = 'N'
        elif dir == 'S':
            x = x + 1
            dir = 'E'
        else:
            raise ValueError("Something is out of order")
    elif symbol == '|':
        if dir == 'N':
            y = y - 1
        elif dir == 'S':
            y = y + 1
        else:
            raise ValueError("Something is out of order")
    elif symbol == 'L':
        if dir == 'W':
            y = y - 1
            dir = 'N'
        if dir == 'S':
            x = x + 1
            dir = 'E'
        else:
            raise ValueError("Something is out of order")
    elif symbol == 'J':
        if dir == 'S':
            x = x - 1
            dir = 'W'
        elif dir == 'E':
            y = y - 1
            dir = 'N'
        else:
            raise ValueError("Something is out of order")
    elif symbol == '7':
        if dir == 'N':
            x = x - 1
            dir = 'W'
        elif dir == 'E':
            y = y + 1
            dir = 'S'
        else:
            raise ValueError("Something is out of order")
    else:
        raise ValueError("Do not recognise symbol")
    return x, y, dir

steps = 1
symbol = cs[y][x]

while symbol != 'S':
    #print(f"Step: {step}, symbol: {symbol}")
    steps += 1
    x, y, dir = step(x, y, dir, symbol)
    symbol = cs[y][x]
    

print(f"Steps: {steps/2}")