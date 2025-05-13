import random
from model import get_class

character = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


panjang_character = int(input("Masukan Panjang Password:"))

password = ""
10
for i in range(panjang_character):
    random_character = random.choice(character)
    password += random_character

print(password)

