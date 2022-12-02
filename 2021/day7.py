filename = 'day7.txt'
data = [int(i) for i in open(filename, 'r').read().split(',')]

results = {}
for position in range(min(data), max(data)+1):
    fuel = 0
    fuelsteps = 0
    for submarine in data:
        fuel += abs(submarine - position)
    results[position] = fuel

print('Minimum fuel:', min(results.values()))

### Part Two ###

results = {}
for position in range(min(data), max(data)+1):
    fuel = 0
    fuelsteps = 0
    for submarine in data:
        fuelsteps = abs(submarine - position)
        fuel += fuelsteps*(fuelsteps+1)/2
    results[position] = fuel

print('Minimum fuel:', min(results.values()))