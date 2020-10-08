n = int(input())
open_brackets = 0
closed_brackets = 0
unbalanced = False
for i in range(1, n + 1):
    another_str = input()
    if another_str == "(":
        open_brackets += 1
    elif another_str == ")":
        closed_brackets += 1
        if not open_brackets - closed_brackets == 0:
            unbalanced = True
if not open_brackets == closed_brackets:
    unbalanced = True

if unbalanced == True:
    print("UNBALANCED")
else:
    print("BALANCED")