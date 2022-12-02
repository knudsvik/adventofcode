filename = '2022/day1.txt'

lines = open(filename, 'r').readlines()

calories = 0
manifest = []
for line in lines:
    if not line == '\n':
        calories += int(line)
    else:
        manifest.append(calories)
        calories = 0

print('Max calories: ', max(manifest))

## Part two

manifest.sort()

print('Sum of the three: ', sum(manifest[-3:]))