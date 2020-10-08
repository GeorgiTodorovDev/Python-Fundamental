n = int(input())
result = 0
for num in range(1, n + 1):
    letter = input()
    result += ord(letter)
print(f'The sum equals: {result}')