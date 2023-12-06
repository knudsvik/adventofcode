from functools import reduce

races = {1: [7, 9],  # Test
         2: [15, 40],
         3: [30, 200]
         }

races = {1: [48, 390],
         2: [98, 1103],
         3: [90, 1112],
         4: [83, 1360]
         }


def distance(hold_time, total_time):
    velocity = hold_time
    race_time = total_time - hold_time
    return race_time * velocity

results = []

for race in races:
    total_time, record = races[race]
    
    ways = 0
    i = 0  # time

    for hold_time in range(total_time):
        result = distance(hold_time, total_time)
        if result > record:
            ways += 1
    
    results.append(ways)


print(f"Part 1: {reduce(lambda x, y: x * y, results)}")

## PART TWO

total_time, record = 71530, 940200  # Test
total_time, record = 48989083, 390110311121360
    
ways = 0
i = 0  # time

for hold_time in range(total_time):
    result = distance(hold_time, total_time)
    if result > record:
        ways += 1
    
print(f"Part 2: {ways}")