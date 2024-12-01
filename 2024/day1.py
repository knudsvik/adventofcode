filename = '2024/input/day1.txt'
lines = open(filename, 'r').readlines()

left, right = [], []

for line in lines:
    left.append(int(line.split()[0].strip()))
    right.append(int(line.split()[1].strip()))

left.sort()
right.sort()

result = 0

for i in range(len(left)):
    result += abs(left[i]-right[i])

print(f"Part 1: {result}")

## Part 2

result = sum(right.count(num) * num for num in left)

print(f"Part 2: {result}")