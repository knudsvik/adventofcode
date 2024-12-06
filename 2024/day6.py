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
        return True
    elif direction == 'E' and x == cs_width:  # Heading East at the right border
        return True
    elif direction == 'S' and y == cs_height:  # Heading South at the bottom border
        return True
    elif direction == 'W' and x == 0:  # Heading West at the left border
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
print(f"Visits in part 1: {count}")

# part two

obstacles = 0

cs = [list(line.strip()) for line in lines]
end_of_cs = False
x, y = Sx, Sy

steps = 0

for col in range(cs_width + 1):

    for row in range(cs_height + 1):

        #print(f"Column: {col}, Row: {row}")

        #if col == 6 and row == 7:
        #    pass

        if cs[row][col] != '#':
            cs[row][col] = '#'

            while end_of_cs != True and steps < 20000:
                dx, dy = movement[directions[direction_index]]
                if cs[y + dy][x + dx] != '#':
                    x, y = x + dx, y + dy
                    cs[y][x] = 'X'
                else:
                    direction_index = (direction_index + 1) % len(directions)
                steps += 1
                end_of_cs = check_end(x, y, directions[direction_index])
            if steps == 20000:
                obstacles += 1
                #print(f"Obstacle set in x: {col}, y: {row}")
            steps = 0
            end_of_cs = False
            x, y = Sx, Sy
            direction_index = 0 
            cs[row][col] = '.'

print(f"Possible obstacles: {obstacles}")