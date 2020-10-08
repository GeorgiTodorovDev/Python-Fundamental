# number = float(input())
# while number < 1 or number > 100:
#     number = float(input())
# print(f"The number {number} is between 1 and 100")

number = float(input())
while not (number >= 1 and number <= 100):
    number = float(input())
print(f"The number {number} is between 1 and 100")
# Tuk tynkiq moment e v while cikyla vyprosnto NOT raboti samo za promenlivata sled neq, za tova sym iznesyl celiq izraz v skobi.
#Varianta tuk beshe da sloja 2 ro NOT predi 2rata promenliva number