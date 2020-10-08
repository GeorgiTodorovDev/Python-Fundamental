n = int(input())
capacity = 0
counter = 0

while counter < n:
    counter += 1
    num = int(input())
    if (capacity + num) <= 255:
        capacity += num
    else:
        print("Insufficient capacity!")
print(capacity)

# n = int(input())
# filled_qnt = 0
#
# for i in range(n):
#     pour = int(input())
#     filled_qnt += pour
#     if filled_qnt >= 255:
#         print("Insufficient capacity!")
#         filled_qnt -= pour
#         continue
# print(filled_qnt)