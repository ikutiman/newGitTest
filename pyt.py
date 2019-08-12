import random

chars = "();@absdefghijklmnopqistuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,-"
length = input("password length ? ")
amount = input("How many password you want to create ?")
amount = int(amount)
length = int(length)
pin = ""
for p in range(amount):
    pin = ""
    for c in range(length):
        pin += random.choice(chars)
    print(pin)

