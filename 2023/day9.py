filename = '2023/input/day9.txt'
lines = open(filename, 'r').readlines()

sum = 0
sum2 = 0

for line in lines:
    history = [int(num) for num in line.split()]

    collection = [history]
    
    temp = ["a"]
    while any(element != 0 for element in temp):

        temp = []
        for i in range(len(history) - 1):
            temp.append(history[i+1] - history[i])

        collection.append(temp)
        history = temp
    
    # Start predictions:
    prediction = 0
    pred2 = 0
    for i in range(len(collection)):
        sublist = collection[-i -1]
        prediction += sublist[-1]
        pred2 = sublist[0] - pred2

    sum += prediction
    sum2 += pred2

print(sum)
print(sum2)