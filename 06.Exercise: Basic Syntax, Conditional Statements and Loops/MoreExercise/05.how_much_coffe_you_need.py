word = ["coding", "dog", "cat", "movie", "CODING", "DOG", "CAT", "MOVIE"]
our_input = input()
coffe = 0
while not our_input == "END":
    if word.count(our_input) == 1:
        if our_input.isupper() == True:
            coffe += 2
        else:
            coffe += 1
    our_input = input()
if coffe > 5:
    print("You need extra sleep")
else:
    print(coffe)