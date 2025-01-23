class Zoldsegek: 
    def __init__(self):
        self.lista = []

    def beolvasas(self):
        with open ("zoldsegek.txt", "r", encoding="UTF8") as file: 
            adatok = file.readlines()

            for adat in adatok: 
                adat = adat.strip()
                adat = adat.split(";")


                zoldseg = adat[0]
                tonna = int(adat[1])
                ar = int(adat[2])
                ev = int(adat[3])

                self.lista.append([zoldseg, tonna, ar, ev])

            print("A teljes fájl tartalma:")
            
            for list in self.lista: 
                print(f"{list[0]} - {list[1]} tonna {list[2]} Ft/kg - {list[3]}")

            
    def termesuk_2015_utan(self):
        print("A 2015 utáni zöldségek:")
        for termes in self.lista:
            if termes[3] > 2015:
                print(f"{termes[0]} - {termes[1]} tonna {termes[2]} Ft/kg - {termes[3]}")



    def legolcsobb(self):

        legolcsobb = float("inf")
        legolcsobb_zoldseg = " "

        print("A legolcsóbb zöldség: ")
        for olcso in self.lista: 
            if olcso[2] < legolcsobb: 
                legolcsobb = olcso[2]
                legolcsobb_zoldseg = olcso[0]
        
        print(f"{legolcsobb_zoldseg} - {legolcsobb} Ft/Kg")

    
    def paprika_kezdes(self):

        with open ("paprika_zoldsegek.txt", "w", encoding = "UTF8") as file: 
           
            megszamol = 0
        print("--------------------------------------------------")
        for p in self.lista: 
                if p[0].startswith("Paprika"):
                    megszamol += 1 
            
                print(f"{p[0]} - {p[1]} tonna {p[2]} Ft/kg - {p[3]}")
                file.write(f"{p[0]} - {p[1]} tonna {p[2]} Ft/kg - {p[3]}")
        print(f"'Paprika'-val kezdődő zöldségek száma: {megszamol}")



etelek = Zoldsegek()
etelek.beolvasas()
etelek.termesuk_2015_utan()
etelek.legolcsobb()
etelek.paprika_kezdes()

