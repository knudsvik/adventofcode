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
    #print(f"Update: {update}")
    update = update.split(',')

    a = True
    
    for item in range(len(update)):
        while a:
            #print(f"Checking {update[item]}")
            if int(update[item]) in ruleset:
                page_rules = ruleset[int(update[item])]
                #print(f"Page rules: {page_rules}")
                for other in range(item + 1, len(update)):
                    #print(f" - Checking this remaining number: {update[other]}")
                    if int(update[other]) in page_rules:
                        #print("Oh no")
                        a = False
                        break
                    #else:
                        #print("all good")  
            break   
    if a == True:
        result.append(int(update[len(update) // 2]))  # If not breaking rules 
        #print("- - Result added") 
    
print(f"Result: {sum(result)}")