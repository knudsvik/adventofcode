filename = 'day3.txt'
rucksacks = open(filename, 'r').readlines()

lower = {chr(i+96):i for i in range(1,27)}
upper = {chr(i+64):i for i in range(1,27)}
for key in upper:
  upper[key] += 26
priorities = {**lower, **upper}

priority = 0

for sack in rucksacks:
    compartment1 = sack[:len(sack)//2]
    compartment2 = sack[len(sack)//2:]
    sack_prio = []
    for item in compartment1:
        if item in compartment2:
            sack_prio.append(priorities[item])
    priority += sum(sack_prio) / float(len(sack_prio))

print('Priority: ', priority)

## Part two
priority = []

elf = 0
while True:
    badges = []
    for item in rucksacks[elf]:
        if item in rucksacks[elf+1] and item in rucksacks[elf+2] and item is not '\n':
            badges.append(priorities[item])
    priority.append(badges[0])
    elf += 3
    if elf >= len(rucksacks):
        break

print('Badge priority: ',sum(priority))





