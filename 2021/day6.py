import numpy as np

filename = 'day6_sample.txt'
data = [int(i) for i in open(filename, 'r').read().split(',')]

def fish(days):
    current = np.array(data)
    for day in range(1,days+1):
        current[current == 0] = 999
        current -= 1
        current[current == 998] = 6
        if not day == 1:
            current = np.append(current, [8]*new)
        new = np.count_nonzero(current == 0)
        print('day ', day, ': ', len(current))
    return len(current)
    
#fish(80)

## PART 2 ##

import math

def lanternfish(days):
    initial = np.array(data)
    total = 0 # len(initial)
    cycles_total = int(days / 7)
    cycles_rest = days % 7
    for fish in initial:
        fish_cycles = cycles_total
        if fish <= cycles_rest:
            fish_cycles += 1
        spawned = math.factorial(fish_cycles)
        total += spawned
    return total

lanternfish(8)