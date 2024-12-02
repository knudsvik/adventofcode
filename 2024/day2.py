filename = '2024/input/day2.txt'
reports = open(filename, 'r').readlines()

safe = 0

for report in reports:
    print(report)
    report = list(map(int, report.split()))

    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    valid_differences = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

    if (is_increasing or is_decreasing) and valid_differences:
        print("Safe report detected!")
        safe += 1
       

print(f'There are {safe} safe reports')