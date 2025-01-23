nev = input("Adja meg a tábor nevét: ")

kaloria = int(input("Adjon meg egy napi kaloriaértéket "))
kaloriak = []

db = 0

while True: 
    kaloria = int(input("Adjon meg egy napi kaloriaértéket (jelenlegi adatok száma: {db} )"))
    kaloriak.append(kaloria)
    db += 1

    if db > 5: 
        kerdes = input("Szeretne további kalóriákat hozzáadni? (i/n): ").lower()
        if kerdes == "n":
            break

print("=======Heti Kalóriaösszegzés =========")
print(f"Tábor neve: {nev}")
print(f"Átlagosan elégetett kalória naponta: {sum(kaloriak)/len(kaloriak)} kcal")