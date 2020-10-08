key = int(input())
n = int(input())
for i in range(n):
    letter = input()
    b = ord(letter)
    result = chr(b + key)
    print(result, end="")

# a = "a"
# b = ord(a)
# c = chr(b + 3)
# print(b)
# print(c)


# key = int(input())
# n = int(input())
# counter = 0
# while counter < n:
#     counter += 1
#     letter = input()
#     b = ord(letter)
#     result = chr(b + key)
#     print(result, end="")