from datetime import datetime

class Virágbolt:
    def __init__(self):
        self.lista = []
    
    def beolvas(self):
        with open("viragok.txt", "r", encoding="UTF8") as fajl:
            adatok = fajl.readlines()

            for adat in adatok:

                adat = adat.strip().split(",")

                virag = adat[0]
                ar = int(adat[1])
                mennyiseg = int(adat[2])
                # szallitas = datetime.strptime(adat[3]," %Y-%m-%d")
                szallitas = adat[3]
                self.lista.append([virag, ar, mennyiseg, szallitas])
            
            for item in self.lista:
                print(f"{item[0]}, {item[1]} Ft, {item[2]} darab, Szállítás: {item[3]}")

    def legdragabb(self):
        legdragabb_ar = 0
        legdragabb_virag = ""
        for dragabb in self.lista:
            if dragabb[1] > legdragabb_ar:
                legdragabb_ar = dragabb[1]
                legdragabb_virag = dragabb[0]
        
        print(f"\nA legdrágább virág: {legdragabb_virag} - {legdragabb_ar}")

    def atlag(self):
        db_atlaga = []
        for a in self.lista:
            db_atlaga.append(a[2])

        print(f"Az eladott virágok átlagos darabszáma: {round(sum(db_atlaga)/len(db_atlaga))} darab.")

    def r_kezdodik(self):
        megszamol = 0
        with open("R_betus_viragok.txt", "w", encoding="UTF8") as file:
            for r in self.lista:
                if r[0].startswith("R"):
                    megszamol += 1
                    print(f"{r[0]}, {r[1]} Ft, {r[2]} darab, Szállítás: {r[3]}")
                    file.write("A 'R'-rel kezdődő virágok:")
                    file.write(f"\n{r[0]}, {r[1]} Ft, {r[2]} darab, Szállítás: {r[3]}")

            print(f"\nA 'R'-rel kezdődő virágok száma: {megszamol}")

viragok = Virágbolt()
viragok.beolvas()
viragok.legdragabb()
viragok.atlag()
viragok.r_kezdodik()




