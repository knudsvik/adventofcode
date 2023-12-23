filename = '2023/input/day15.txt'

debug = False
test = False

input = open(filename, 'r').read()
steps, no_boxes = input.split(sep=','), 256

if test:
    steps, no_boxes = ["rn=1","cm-","qp=3","cm=2","qp-","pc=4","ot=9","ab=5","pc-","pc=6","ot=7"], 10

sum = 0

def hash(input):
    current = 0
    for character in input:
            current += ord(character)
            current = current * 17
            current = current % 256
    return current

for step in steps:
     sum += hash(step)

print(f"Part 1: {sum}")

# PART TWO

import re

class Box:
    def __init__(self, name):
        self.name = "Box" + str(name)
        self.lenses = []
        self.box_no = name

    def focus_power(self):
        power = 0
        if len(self.lenses) > 0:
            for slot, lens in enumerate(self.lenses):
                 lens_power = (self.box_no + 1) * (slot + 1) * int(lens.split()[1])
                 power += lens_power
                 if debug == True:
                    print(f"{self.name}, slot {slot}: Focus power: {lens_power}")
        return power
            
    
boxes = []

for i in range(no_boxes):
    boxes.append(Box(i))

for step in steps:
    if step == "qp-":
         pass
    match = re.match(r'([a-zA-Z]+)([=-]?)(.*)', step)
    label = match.group(1)
    box_no = hash(label)

    operation = match.group(2)
    if operation == "=":
         replaced = False
         lens = match.group(3)
         for i, inserted in enumerate(boxes[box_no].lenses):
             if inserted.startswith(label):
                  boxes[box_no].lenses[i] = str(label + " " + lens)
                  replaced = True      
                  break     
         if not replaced:
              boxes[box_no].lenses.append(str(label + " " + lens))
    elif operation == "-":
        for inserted in reversed(boxes[box_no].lenses):
             if inserted.startswith(label):
                  boxes[box_no].lenses.remove(inserted)
    else:
         raise ValueError
    
    if debug:
        print(f"After {step}:")
        for box in boxes:
            if len(box.lenses) > 0:
                print(f" -- {box.name}: {box.lenses}")
        print(" ")

focus_power = 0
for box in boxes:
     focus_power += box.focus_power()

print(f"Part 2: {focus_power}")
