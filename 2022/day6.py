filename = 'day6.txt'
with open(filename) as file:
   input = file.read()

marker = 0
while marker == 0:
    for subset in range(len(input)):
        sub = []
        for character in range(0,4):
            sub.append(input[subset+character])
        if len(sub) == len(set(sub)):
            marker = subset + 4
            break

print('The first marker is in position: ', marker)


# Part two

message = 0
while message == 0:
    for subset in range(len(input)):
        sub = []
        for character in range(0,14):
            sub.append(input[subset+character])
        if len(sub) == len(set(sub)):
            message = subset + 14
            break

print('The first message marker is in position: ', message)