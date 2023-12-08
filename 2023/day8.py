filename = '2023/input/day8.txt'
lines = open(filename, 'r').readlines()

directions = lines[0].strip('\n')
nodes = {}

for line in lines[2:]:
    nodes[line[:3]] = line.split('=')[1].strip()[1:-1].split(', ')

elements = nodes['AAA']
steps = 0
node = "someBullshit"

while node != 'ZZZ':
    for direction in directions:
        if direction == 'L':
            node = elements[0]
        elif direction == 'R':
            node = elements[1]
        steps += 1
        if node == 'ZZZ':
            break
        elements = nodes[node]

print(steps)