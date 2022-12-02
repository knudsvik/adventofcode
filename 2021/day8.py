filename = 'day8.txt'
data = open(filename, 'r').read().split('\n')

total = 0
for i in data:
    segment = i.split('|')[1]
    for signal in segment.split(' '):
        a = len(signal)
        if 2 <= a <= 4 or a == 7:
            total += 1

## Part Two ##

for i in data:
    segment = i.split('|')[1]
    for signal in segment.split(' '):
        a = len(signal)
        if 2 <= a <= 4 or a == 7:
            total += 1

test = 'fdgacbe cefdb cefbgd gcbe'

result = ''
for i in test.split(' '):
    if len(i) == 2:
        number = 1
    elif len(i) == 4:
        number = 4
    elif len(i) == 3:
        number = 7
    elif len(i) == 7:
        number = 8
    if len(i) == 5:
        
    result += str(number)

cdfbe: 5
gcdfa: 2
fbcad: 3

cefabd: 9
cdfgeb: 6
cagedb: 0
