with open("input.txt") as file:
    lines = file.readlines()

safe_reports = 0
for report in lines:
    report_levels = [int(num) for num in report.split(" ")]
    unsafe_count = 0
    is_increasing = report_levels[0] - report_levels[1] < 1
    for i in range(len(report_levels) - 1):
        diff = (report_levels[i] - report_levels[i + 1])
        diff = diff * -1 if is_increasing else diff
        if diff < 1 or diff > 3:
            unsafe_count += 1
            if unsafe_count > 1:
                break

    if unsafe_count <= 1:
        safe_reports += 1

print(safe_reports)
