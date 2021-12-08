import numpy as np

filename = 'day4_sample.txt'

data = open(filename, 'r').read().split('\n')


draw = data[0]
boardsize = len([int(x) for x in data[-1].split() if x.isdigit()])
boards = []
for i in range(1, len(data)):
    if data[i] != '':
        board = np.ndarray(shape=(boardsize,boardsize), dtype=int)
        while data[i-1] = '':
            board = np.ndarray(shape=(boardsize,boardsize), dtype=int)
            row = [int(x) for x in data[i].split() if x.isdigit()]
            
            for number in data[i].split(' '):

            board = np.arrray
            boards.append(board)


