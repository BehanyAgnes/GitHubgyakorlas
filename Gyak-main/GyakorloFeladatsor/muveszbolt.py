lista = []

with open ("termekek.txt", "r", encoding="UTF-8") as file:

    elso_sor = file.readline() 
    sorok = file.readlines()

    for sor in sorok: 
        sor = sor.strip()
        sor = sor.split(";")

        termek = sor[0]
        ar = int(sor[1])
        eladott_mennyiseg = int(sor[2])
        ev = int(sor[3])

        lista.append([termek, ar, eladott_mennyiseg, ev])

print(lista)

for item in lista: 
    print(f"{item[0]}, {item[1]}, {item[2]}, {item[3]}")

legdragabb = lista[0]

for item in lista: 
    if item[1] > legdragabb[1]:
        legdragabb = item

print(f"A legdrágább termék: {legdragabb[0]} ({legdragabb[1]} Ft)")

# print(type(item[2]))

szamlalo = 0

for item in lista: 

    szamlalo += item[2]

print(f"Az eladott termékek darabszámának átlaga: {round(szamlalo/len(lista))} db")

C_betus = []
osszeg = 0

for item in lista: 

    if item[0].startswith("C"):
        C_betus.append(item[0])

for i in C_betus:
    osszeg +=1

print(f"'C'-vel kezdődő termékek száma: {osszeg}")
print(f"'C'-vel kezdődő termékek: {C_betus}")

with open("C_betus_termekek.txt", "w", encoding="UTF-8") as file:
    file.write(f"'C'-vel kezdődő termékek: {C_betus}")







