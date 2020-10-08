# word = input()
# word_len = len(word)
# reversed_word = ""
# for index in range(word_len -1, -1, -1):
#     reversed_word += word[index]
# print(reversed_word)

#######################

# word = input()
# for index in range(len(word)-1,-1,-1):
#     print(word[index], end="")
#Komentar end prosto ne pozvolqva na kursora da sleze na noviq red a ostava na syshtiq ,koeto dolepq edno do drugo simvolite , vmesto da gi svalq na nov red

######################

# word = input()
# print(word[::-1])

######################

word = input()
reversed_word = ""
for index in range(len(word)-1,-1,-1):
    reversed_word += word[index]
print(reversed_word)