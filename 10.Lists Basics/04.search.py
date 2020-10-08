n = int(input())
word = input()
result = []
result_word = []
for index in range(n):
    words = input()
    result.append(words)
    if word in words:
        result_word.append(words)
print(result)
print(result_word)