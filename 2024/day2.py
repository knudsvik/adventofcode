filename = '2024/input/day2.txt'
reports = open(filename, 'r').readlines()

safe = 0

for report in reports:
    report = list(map(int, report.split()))

    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    valid_differences = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

    if (is_increasing or is_decreasing) and valid_differences:
        safe += 1
       

print(f'There are {safe} safe reports in part one')

## Part two

safe = 0

for report in reports:
    report = list(map(int, report.split()))

    for i in range(len(report)):

        temp_report = report.copy()
        temp_report.pop(i)
        is_increasing = all(temp_report[i] < temp_report[i + 1] for i in range(len(temp_report) - 1))
        is_decreasing = all(temp_report[i] > temp_report[i + 1] for i in range(len(temp_report) - 1))
        valid_differences = all(1 <= abs(temp_report[i] - temp_report[i + 1]) <= 3 for i in range(len(temp_report) - 1))

        if (is_increasing or is_decreasing) and valid_differences:
            safe += 1
            break

print(f'There are {safe} safe reports in part two')
