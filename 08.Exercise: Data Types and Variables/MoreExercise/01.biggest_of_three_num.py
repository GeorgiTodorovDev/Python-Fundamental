import sys

num = 3
counter = 0
max_value = -sys.maxsize - 1
while counter < num:
    counter += 1
    number = int(input())
    if number > max_value:
        max_value = number
print(max_value)