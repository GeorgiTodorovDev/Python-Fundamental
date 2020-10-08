n = int(input())

positive_num = []
negative_num = []

for index in range(n):
    num = int(input())
    if num < 0:
        negative_num.append(num)
    else:
        positive_num.append(num)

print(f'{positive_num}\n{negative_num}\nCount of positives: {len(positive_num)}. Sum of negatives: {sum(negative_num)}')