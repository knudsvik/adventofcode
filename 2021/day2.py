filename = 'day2.txt'

data = open(filename, 'r').read().split('\n')

x = 0
z = 0
for i in data:
    value = int(i[-1:])
    if 'forward' in i:
        x += value
    elif 'up' in i:
        z -= value
    elif 'down' in i:
        z += value

print('Part 1: ', x*z)

## Part 2 ##

aim = 0
x = 0
z = 0
for i in data:
    value = int(i[-1:])
    if 'down' in i:
        aim += value
    elif 'up' in i:
        aim -= value
    elif 'forward' in i:
        x += value
        if aim > 0:
            z += aim * value
        elif aim < 0:
            z -= aim * value

print('Part 2: ', x*z)

