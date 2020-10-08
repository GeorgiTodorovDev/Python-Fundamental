string = input()
store_list = []
counter = 0
result = []
for char in string:
    if char.isupper():
        result.append(counter)
    counter +=1
print(result)