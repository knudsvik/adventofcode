import re
import math

filename = '2024/input/day3.txt'
memory = open(filename, 'r').readlines()

text = memory[0]

pattern = r"mul\(\d+,\d+\)"

matches = re.findall(pattern, memory[0])

result = 0

for match in matches:
    numbers = re.findall(r'\d+', match)
    numbers = list(map(int, numbers))
    result += math.prod(numbers)

print(result)