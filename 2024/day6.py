filename = '2024/input/day6.txt'
lines = open(filename, 'r').readlines()

# Coordinate system:
cs = [list(line.strip()) for line in lines]

cs_width = len(cs[0]) - 1
cs_height = len(cs) - 1

directions = ['N', 'E', 'S', 'W']
movement = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
}

# Check if the next move goes out of bounds
def check_end(x, y, direction):
    if direction == 'N' and y == 0:  # Heading North at the top border
        print("going out")
        return True
    elif direction == 'E' and x == cs_width:  # Heading East at the right border
        print("going out")
        return True
    elif direction == 'S' and y == cs_height:  # Heading South at the bottom border
        print("going out")
        return True
    elif direction == 'W' and x == 0:  # Heading West at the left border
        print("going out")
        return True
    return False

# Find start:
for Sy, line in enumerate(lines):
    if '^' in line:
        Sx = line.find('^')
        #print(f"{cs[Sy][Sx]} is in line: {Sy}, position: {Sx}")
        break

x, y = Sx, Sy

cs[y][x] = 'X'
direction_index = 0   # North

end_of_cs = False

while end_of_cs != True:
    dx, dy = movement[directions[direction_index]]
    if cs[y + dy][x + dx] != '#':
        x, y = x + dx, y + dy
        cs[y][x] = 'X'
    else:
        direction_index = (direction_index + 1) % len(directions)
    end_of_cs = check_end(x, y, directions[direction_index])
    

count = sum(row.count('X') for row in cs)
print(f"Visits: {count}")

