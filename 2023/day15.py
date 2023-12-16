filename = '2023/input/day15.txt'

input = open(filename, 'r').read()
steps = input.split(sep=',')

#input = ["H", "A", "S", "H"]
#steps = ["rn=1","cm-","qp=3","cm=2","qp-","pc=4","ot=9","ab=5","pc-","pc=6","ot=7"]

sum = 0

for step in steps:
    current = 0
    for character in step:
        current += ord(character)
        current = current * 17
        current = current % 256
    sum += current

print(sum)