import random

print("Add meg a 3 kedvenc állatodat!")

allatok = []

while len(allatok) < 3: 
    allat = input(f"Adj meg egy kedvenc állatot: ({len(allatok)+1} :)")
    allatok.append(allat)
    print(f"{len(allatok)}. {allat} került hozzáadásra a listához.")

print("A kedvenc állataid:")

print(f"{allatok[0]}, {allatok[1]}, {allatok[2]}")

kedvenc_allat = random.choice(allatok)
print(f"A kiválasztott kedvenc állat: {kedvenc_allat}")