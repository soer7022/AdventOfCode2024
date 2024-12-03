import re

with open('input.txt') as file:
    text = file.read()

lines_to_parse = []

to_check = text.split("do()")
for item in to_check:
    lines_to_parse.append(item.split("don't()")[0])


total = 0
for line in lines_to_parse:
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    for match in matches:
        left, right = match.split(",")
        left = int(left.split("(")[1])
        right = int(right.split(")")[0])
        total += left * right

print(total)
