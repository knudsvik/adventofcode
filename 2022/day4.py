filename = 'day4.txt'
elves = open(filename, 'r').readlines()

fully_contained = 0
overlap = 0

for pair in range(0, len(elves)):
    sectors = elves[pair].rstrip('\n').split(',')
    elf1 = sectors[0]
    elf2 = sectors[1]
    a = False
    b = False
    elf1_sections = []
    elf2_sections = []
    for section in range(int(elf1.split('-')[0]), int(elf1.split('-')[1])+1):
        elf1_sections.append(section)
    for section in range(int(elf2.split('-')[0]), int(elf2.split('-')[1])+1):
        elf2_sections.append(section)
    if all([item in elf2_sections for item in elf1_sections]):
        fully_contained += 1
        a = True
    if all([item in elf1_sections for item in elf2_sections]):
        fully_contained += 1
        b = True
    if a and b:
        fully_contained -= 1
    if any([item in elf1_sections for item in elf2_sections]):
        overlap += 1

print('Fully contained: ', fully_contained)
print('Overlaps: ', overlap)