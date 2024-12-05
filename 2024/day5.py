import re

filename = '2024/input/day5.txt'
data = open(filename, 'r').read()
data = re.split(r'\n\s*\n', data)

# Rules
rules = data[0].split()
ruleset = {}

for rule in rules:
    before, after = rule.split('|')
    before = int(before)
    after = int(after)

    if after in ruleset:
        ruleset[after].append(before)
    else:
        ruleset[after] = [before]


# Updates
updates = data[1].split()

result = []

for update in updates:
    update = update.split(',')

    a = True
    
    for item in range(len(update)):
        while a:
            if int(update[item]) in ruleset:
                page_rules = ruleset[int(update[item])]
                for other in range(item + 1, len(update)):
                    if int(update[other]) in page_rules:
                        a = False
                        break
            break   
    if a == True:
        result.append(int(update[len(update) // 2]))  

print(f"Result: {sum(result)}")
