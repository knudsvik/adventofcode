import re

filename = '2024/input/day7_s.txt'
data = open(filename, 'r').readlines()

for equation in data:
    result, values = equation.split(':')
    values = list(map(int, values.split()))

    for trial in range(values):
        

pass