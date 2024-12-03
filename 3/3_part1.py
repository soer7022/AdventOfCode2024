import re

with open('input.txt') as file:
    lines = file.readlines()

total = 0
for line in lines:
    matches = re.findall(r'mul\(\d+,\d+\)',line)
    for match in matches:
        left,right = match.split(",")
        left = int(left.split("(")[1])
        right = int(right.split(")")[0])
        total += left*right

print(total)