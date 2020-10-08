my_string = input()
case_my_string = my_string.lower()
counter = 0

if case_my_string.find("sand") != -1:
    counter += case_my_string.count("sand")
if case_my_string.find("water") != -1:
    counter += case_my_string.count("water")
if case_my_string.find("fish") != -1:
    counter += case_my_string.count("fish")
if case_my_string.find("sun") != -1:
    counter += case_my_string.count("sun")

print(counter)
