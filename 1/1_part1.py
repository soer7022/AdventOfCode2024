
with open("input.txt") as file:
    lines = file.readlines()

total = 0
numbers_left = []
numbers_right = []
for line in lines:
    left,right = [int(num) for num in line.split(" ") if num != ""]
    numbers_right.append(right)
    numbers_left.append(left)

numbers_left.sort()
numbers_right.sort()

for i in range(len(numbers_left)):
    total += abs(numbers_left[i] - numbers_right[i])

print(total)
