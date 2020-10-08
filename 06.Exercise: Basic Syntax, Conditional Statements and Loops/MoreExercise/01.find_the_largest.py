# number = int(input())
# str_number = str(number)
# result = []
# for char in str_number:
#     result.append(char)
# new_result = sorted(result, reverse=True)
# final_result = ""
# for char2 in new_result:
#     final_result += char2
# int_final_result = int(final_result)
# print(int_final_result)



number = input()
test = sorted(number)[::-1]
for i in test:
    print(int(i), end='')