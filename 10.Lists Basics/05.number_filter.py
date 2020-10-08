n = int(input())

is_even = []
is_odd = []
is_negative = []
is_positive = []

for index in range(n):
    num = int(input())
    if num % 2 == 0:
        is_even.append(num)
    if not num % 2 == 0:
        is_odd.append(num)
    if num < 0:
        is_negative.append(num)
    if num >= 0:
        is_positive.append(num)

command = input()
if command == "even":
    print(is_even)
if command == "odd":
    print(is_odd)
if command == "negative":
    print(is_negative)
if command == "positive":
    print(is_positive)
