#blinks, data = 1, '0 1 10 99 999'
#blinks, data = 6, '125 17'
#blinks, data = 25, '125 17'
#blinks, data = 25, '0 27 5409930 828979 4471 3 68524 170'
blinks, data = 75, '0 27 5409930 828979 4471 3 68524 170'

stones = a_int = [int(x) for x in data.split()]

blink = 0

while blink < blinks:
    blink += 1
    print(f"Blink: {blink}")

    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            value = str(stones[i])
            mid_index = len(value) // 2
            stones[i:i+1] = [int(value[:mid_index]), int(value[mid_index:])]
            i += 1
        else:
            stones[i] = stones[i] * 2024    
        i += 1

print(f"There are now {len(stones)} stones:")
#print(stones)
