filename = 'day3.txt'
data = open(filename, 'r').read().split('\n')

bitlength = len(data[0])
g = [0] * bitlength
gamma = g.copy()
epsilon = g.copy()
datasize = len(data)

for i in data:
    for bit in range(0, bitlength):
        if int(i[bit]) == 1:
            g[bit] += 1

for j in range(0, len(g)):
    if g[j] > datasize/2:
        gamma[j] = 1
        epsilon[j] = 0
    else:
        gamma[j] = 0
        epsilon[j] = 1

def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))


print('gamma rate: ', binatodeci(gamma))
print('espilon rate: ', binatodeci(epsilon))
print('Power consumption: ', binatodeci(gamma)*binatodeci(epsilon))

### PART 2 ###

import numpy as np
filename = 'day3_small.txt'
data = open(filename, 'r').read().split('\n')

# making matrix
matrix = [0] * len(data)
for line in range(len(data)):
    row = data[line]
    datapoint = []
    for bit in row:
        datapoint.append(int(bit))
    matrix[line] = datapoint
new = np.array(matrix)

for bit in range(bitlength):
    if not sum(new[:,bit]) >= new[:,bit].size:
        #gjør noe



g = [0] * bitlength
dominator = [0] * bitlength

for bit in range(0, bitlength):
    column = 0
    rows = 0
    for row in data:
        if int(row[bit]) == 1:
            column += 1
        rows += 1
    if column >= rows / 2:
        dominator[bit] = 1
    else:
        dominator[bit] = 0
            



for i in data:
    for bit in range(0, bitlength):
        if int(i[bit]) == 1:
            g[bit] += 1



oxygen = [0] * bitlength
lastcolumn = [1] * len(data)

for bit in range(0, bitlength):
    x = 0
    rows = 0
    for row in data:
        

        if int(row[bit]) == 1 and lastcolumn[rows] == 1:
            x += 1
            lastcolumn[rows] = 1
        rows += 1
    if x >= rows / 2:
        oxygen[bit] = 1
    else:
        oxygen[bit] = 0
    