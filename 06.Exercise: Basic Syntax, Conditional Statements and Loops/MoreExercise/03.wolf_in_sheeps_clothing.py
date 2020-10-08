my_string = input()
my_list = my_string.split(", ")
len_my_list = len(my_list)

if my_list[(len_my_list - 1)] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for elemnt in my_list:
        if elemnt == "wolf":
            print(f'Oi! Sheep number {len_my_list - 1}! You are about to be eaten by a wolf!')
            break
        len_my_list -= 1