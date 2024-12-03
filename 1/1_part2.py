with open("input.txt") as file:
    lines = file.readlines()

total = 0
numbers_left = []
numbers_map = {}
for line in lines:
    left, right = [int(num) for num in line.split(" ") if num != ""]
    try:
        numbers_map[right] += 1
    except KeyError:
        numbers_map[right] = 1
    numbers_left.append(left)

for number in numbers_left:
    if number not in numbers_map.keys():
        continue
    total += numbers_map[number] * number

print(total)
