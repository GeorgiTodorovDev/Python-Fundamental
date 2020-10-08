a = int(input())
b = int(input())
print(f'Before:\na = {a}\nb = {b}')
old_a = a

a = b
b = old_a
print(f'After:\na = {a}\nb = {b}')
