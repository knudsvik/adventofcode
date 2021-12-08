import numpy as np

filename = 'day5_sample.txt'
data = open(filename, 'r').read().split('\n')

for i in range(len(data)):
    data[i] = data[i].split(' -> ')
    