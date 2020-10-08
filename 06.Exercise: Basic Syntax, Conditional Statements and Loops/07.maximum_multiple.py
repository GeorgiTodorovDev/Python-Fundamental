divisor = int(input())
bound = int(input())
result = int()
if divisor > 0 and bound > 0:
    for i in range(divisor, bound + 1):
        if i <= bound:
            if i % divisor == 0:
                result = i
    print(result)
