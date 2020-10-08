prime = int(input())

for num in range(1, prime + 1):
    if num > 1:
        if prime % num == 0:
            print('False')
            break
        else:
            print('True')
            break
