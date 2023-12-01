filename = '2023/input/day1.txt'
lines = open(filename, 'r').readlines()

sum = 0

for line in lines:
    nu = ""
    for char in line:
        if char.isdigit():
            nu += char
            break
    for char in reversed(line):
        if char.isdigit():
            nu += char
            break
    sum += int(nu)

print(f"sum part 1: {sum}")

### PART TWO

text_numbers = {"one": 1,
 "two": 2,
 "three": 3,
 "four": 4,
 "five": 5,
 "six": 6,
 "seven": 7,
 "eight": 8,
 "nine": 9}

class BreakLoop(Exception):
    pass

sum = 0

for line in lines:
    try:
        t = ""
        for char in line:
            if char.isdigit():
                front_number = int(char)
                raise BreakLoop
            else:
                t += char
                for key in text_numbers:
                    if key in t:
                        front_number = text_numbers[key]
                        raise BreakLoop
    except BreakLoop:
        pass
    try:
        t = ""
        for char in reversed(line.strip()):
            if char.isdigit():
                back_number = int(char)
                raise BreakLoop
            else:
                t = char + t
                for key in text_numbers:
                    if key in t:
                        back_number = text_numbers[key]
                        raise BreakLoop
    except BreakLoop:
        pass
    
    number = int(str(front_number)+str(back_number))
    sum += number

print(f"sum part 2: {sum}")