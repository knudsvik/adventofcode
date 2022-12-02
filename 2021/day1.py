filename = 'day1.txt'

depths = [int(i) for i in open(filename, 'r').read().split('\n')]

d = 0
for i in range(0, len(depths)):
    if not i == 0:
        if depths[i]-depths[i-1] > 0:
            d += 1
print('Part 1: ', d)

### PART B ###

y = 0
for i in range(0, len(depths)):
    if not i < 3:
        high = depths[i-2:i+1] 
        low = depths[i-3:i]

        if sum(high) - sum(low) > 0:
            y += 1
print('Part 2: ', y)