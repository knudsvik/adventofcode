filename, steps = '2023/input/day21_s.txt', 6
filename, steps = '2023/input/day21.txt', 64
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
cs[Sy][Sx] = "."

prev_coord = [(Sx, Sy)]

def take_step(x, y):

    if (0 <= _x < len(cs[0])) and (0 <= _y < len(cs)) and cs[y][x] != "#":
        current_coord.append((_x, _y))
        cs[_y][_x] = "O"
    return

for step in range(steps):
    #print(f"Step: {step}")
    current_coord = []
    #print(f"---- Step {step} ----")
    #for i in cs:
    #    print(i)
    for coord in prev_coord:
        
        x = coord[0]
        y = coord[1]
        
        # Left:
        _x = x - 1
        _y = y
        take_step(_x, _y)

        # Right:
        _x = x + 1
        _y = y
        take_step(_x, _y)

        # Up:
        _x = x
        _y = y - 1
        take_step(_x, _y)

        # Down:
        _x = x
        _y = y + 1
        take_step(_x, _y)

        cs[y][x] = "."

    prev_coord = list(set(current_coord))

print(f"The Elf can reach {len(set(prev_coord))} garden plots")